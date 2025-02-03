### **String Manipulation, Formatting, and Regular Expressions in DevOps**

In **DevOps**, string manipulation and regular expressions (regex) are crucial for automating workflows, processing logs, managing configurations, and handling system outputs efficiently. Python provides powerful built-in methods and libraries for handling these tasks.

---

## **1. Use Cases of String Manipulation in DevOps**
String operations are widely used in **CI/CD pipelines, log analysis, infrastructure automation, and cloud deployments**.

### **1.1. Parsing Log Files**
DevOps engineers often extract meaningful information from logs to **troubleshoot issues** or **trigger alerts**.

#### **Example: Extracting ERROR Messages from Log Files**
```python
with open("app.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            print(line.strip())  # Print only error lines
```

---

### **1.2. Handling Configuration Files**
DevOps deals with multiple configuration formats like **YAML, JSON, INI, and XML**.

#### **Example: Modifying a JSON Config File Dynamically**
```python
import json

config_data = {
    "database": {"host": "localhost", "port": 5432}
}

# Update database host dynamically
config_data["database"]["host"] = "prod-db.example.com"

with open("config.json", "w") as file:
    json.dump(config_data, file, indent=4)

print("Updated Config:", config_data)
```

---

### **1.3. Extracting System Information**
DevOps engineers often work with **system commands** and extract key data.

#### **Example: Extracting Disk Usage Information**
```python
import os

disk_usage = os.popen("df -h | grep '/dev/sda1'").read()
print(f"Disk Usage: {disk_usage.strip()}")
```

---

## **2. String Formatting in DevOps**
String formatting is important in DevOps for **logging, configuration management, and automation scripts**.

### **2.1. Using f-strings (Python 3.6+)**
```python
server_name = "prod-server"
status = "running"
print(f"Server: {server_name}, Status: {status}")
```

### **2.2. Using `.format()` Method**
```python
print("Server: {}, Status: {}".format(server_name, status))
```

### **2.3. Formatting JSON Output for Better Readability**
```python
json_data = {"name": "DevOps Server", "status": "Active"}
formatted_json = json.dumps(json_data, indent=4)
print(formatted_json)
```

---

## **3. Regular Expressions (Regex) in DevOps**
Regular expressions are used for **text processing, log parsing, and pattern matching**.

### **3.1. Use Cases of Regex in DevOps**
| **Use Case**               | **Example**                           |
|----------------------------|--------------------------------------|
| **Log parsing**            | Extract error codes from logs       |
| **Config validation**      | Check if an IP address is valid     |
| **Automated monitoring**   | Detect unauthorized login attempts  |
| **Data extraction**        | Find email addresses in a file      |

---

### **3.2. Common Regex Patterns**
| **Pattern**         | **Description**                            | **Example Match**        |
|---------------------|------------------------------------------|--------------------------|
| `\d+`              | Match any integer                        | `123`, `4567`            |
| `[A-Za-z]+`        | Match any word                           | `DevOps`, `Server`       |
| `\w+@\w+\.\w+`     | Match an email                           | `user@example.com`       |
| `(\d{1,3}\.){3}\d{1,3}` | Match an IP address             | `192.168.1.1`            |

---

### **3.3. Extracting IP Addresses from Logs**
```python
import re

log_data = """
User logged in from 192.168.1.10
Failed login attempt from 203.0.113.5
"""

ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
ip_addresses = re.findall(ip_pattern, log_data)
print("Extracted IPs:", ip_addresses)
```

---

### **3.4. Validating Email Addresses**
```python
email_pattern = r"^\w+@\w+\.\w+$"
emails = ["admin@example.com", "invalid-email", "user@devops.org"]

for email in emails:
    if re.match(email_pattern, email):
        print(f"Valid Email: {email}")
    else:
        print(f"Invalid Email: {email}")
```

---

### **3.5. Automating Log Monitoring with Regex**
Regex helps detect **security threats, errors, and warnings** in logs.

#### **Example: Finding Failed SSH Login Attempts**
```python
import re

log_lines = [
    "Failed password for invalid user admin from 203.0.113.5 port 22",
    "Accepted password for user devops from 192.168.1.20 port 22",
]

ssh_failed_pattern = r"Failed password for .* from (\d{1,3}\.){3}\d{1,3}"

for log in log_lines:
    if re.search(ssh_failed_pattern, log):
        print(f"Security Alert: {log}")
```

---

## **4. Automating DevOps Tasks Using String Manipulation and Regex**
String processing combined with regex is **powerful for automation** in **CI/CD pipelines, monitoring, and configuration management**.

### **4.1. Parsing CI/CD Pipeline Logs for Errors**
```python
ci_cd_log = """
Build step failed: ERROR at line 45
Build completed successfully
"""

if "ERROR" in ci_cd_log:
    print("Build Failed: Check logs for details")
```

---

### **4.2. Automating Kubernetes Log Analysis**
```python
k8s_logs = """
Pod: web-server-123 Status: Running
Pod: db-server-456 Status: CrashLoopBackOff
"""

failed_pods = re.findall(r"Pod: (.+) Status: (CrashLoopBackOff|Error)", k8s_logs)
print("Pods with Issues:", failed_pods)
```

---

### **4.3. Checking Open Ports in Running Containers**
```python
import os
import re

container_ports = os.popen("docker ps --format '{{.Ports}}'").read()
open_ports = re.findall(r"(\d+)->", container_ports)
print("Open Ports in Containers:", open_ports)
```

---

## **5. Tools That Leverage Regex and String Processing in DevOps**
| **Tool**        | **Usage**                                     |
|----------------|---------------------------------------------|
| **Grep**       | Log file filtering using regex             |
| **Sed/Awk**    | Text manipulation in Linux shell scripts   |
| **Splunk**     | Log analysis using regex-based queries     |
| **ELK Stack**  | Centralized logging with regex-based search |
| **Prometheus** | Log scraping and monitoring using patterns |

---

## **6. Conclusion**
- **String manipulation** helps automate log processing, configuration management, and system monitoring.
- **Regex** is powerful for **log filtering, data extraction, and pattern matching**.
- **Combining Python, Regex, and DevOps tools** leads to efficient automation and monitoring.

🚀 **Would you like a hands-on exercise on regex for log parsing or DevOps automation?**