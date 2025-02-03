### **Detect Unauthorized Login Attempts Using Python**
Unauthorized login attempts can indicate security breaches, brute-force attacks, or credential stuffing. Using **Python**, we can analyze authentication logs (e.g., SSH, web server, or system logs) to detect such attempts.

---

## **1. Detect Unauthorized SSH Login Attempts (Linux / Unix)**
The **auth.log** or **secure** log file stores SSH authentication attempts on Linux-based systems.

### **Example: Detect Failed SSH Logins from /var/log/auth.log**
```python
import re

# Path to SSH authentication log file
log_file_path = "/var/log/auth.log"

# Regular expression to match failed SSH login attempts
ssh_failed_pattern = r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

failed_attempts = {}

# Read log file and extract unauthorized access attempts
with open(log_file_path, "r") as log_file:
    for line in log_file:
        match = re.search(ssh_failed_pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

# Display suspicious IPs with failed login attempts
for ip, count in failed_attempts.items():
    print(f"Suspicious IP: {ip} - Failed Attempts: {count}")
```

### **🛠️ How It Works**
- Reads **/var/log/auth.log** (or **/var/log/secure** on CentOS/RHEL).
- Uses **regex** to find IP addresses of failed SSH login attempts.
- Counts failed login attempts per IP.
- Displays IPs attempting unauthorized access.

---

## **2. Detect Brute-Force Attacks from Web Server Logs (Apache/Nginx)**
Attackers may try multiple usernames/passwords to access a web application.

### **Example: Detect Unauthorized Logins in Apache Logs**
```python
import re

log_file_path = "/var/log/apache2/access.log"

# Pattern to match HTTP 401 Unauthorized attempts
unauthorized_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .* 401'

failed_logins = {}

with open(log_file_path, "r") as log_file:
    for line in log_file:
        match = re.search(unauthorized_pattern, line)
        if match:
            ip = match.group(1)
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

for ip, count in failed_logins.items():
    print(f"Potential attacker: {ip} - Unauthorized Attempts: {count}")
```

### **🛠️ How It Works**
- Reads **Apache/Nginx access logs**.
- Matches **401 Unauthorized HTTP status codes**.
- Counts failed login attempts per IP.
- Identifies potential brute-force attackers.

---

## **3. Detect Unauthorized Access Attempts in Windows Event Logs**
Windows logs failed login attempts under **Event ID 4625**.

### **Example: Detect Windows Failed Login Attempts**
```python
import subprocess
import re

# PowerShell command to get failed login attempts (Event ID 4625)
cmd = 'powershell "Get-EventLog Security | Where-Object {$_.EventID -eq 4625} | Format-List Message"'

output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

# Regex pattern to extract failed login attempt details
failed_login_pattern = r'Account Name:\s+(.+)\s+Failure Reason:\s+(.+)'

failed_attempts = []

for line in output.stdout.split("\n"):
    match = re.search(failed_login_pattern, line)
    if match:
        failed_attempts.append((match.group(1), match.group(2)))

for user, reason in failed_attempts:
    print(f"Failed Login: User={user}, Reason={reason}")
```

### **🛠️ How It Works**
- Uses **PowerShell & Python** to fetch Windows Security logs.
- Filters **Event ID 4625** (failed login events).
- Extracts **username & failure reason**.
- Lists unauthorized login attempts.

---

## **4. Real-Time Monitoring with Fail2Ban (Alternative)**
For real-time detection, integrate Python with **Fail2Ban**, which blocks IPs with excessive failed login attempts.

### **Example: Block Unauthorized IPs with Fail2Ban**
```bash
fail2ban-client status sshd
fail2ban-client set sshd unbanip 203.0.113.5
```

---

## **5. Advanced Features:**
- 🔹 **Send alerts via email or Slack** when an IP exceeds failed login attempts.
- 🔹 **Block attackers** automatically using `iptables` or `fail2ban`.
- 🔹 **Integrate with Splunk or ELK** for centralized log monitoring.

---

## **6. Summary**
| **Method** | **Log Type** | **Detection Method** |
|------------|-------------|----------------------|
| SSH Attack Detection | `/var/log/auth.log` | Failed password attempts |
| Web Brute Force | `access.log` | HTTP 401 Unauthorized |
| Windows Failed Logins | Windows Event Log | Event ID 4625 |
| Real-time Blocking | Fail2Ban | Auto-ban malicious IPs |

🚀 **Need help automating alerts or blocking attackers?** Let me know! 😊