import re

log_data = """
User logged in from 192.168.1.10
Failed login attempt from 203.0.113.5
"""

ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
ip_addresses = re.findall(ip_pattern, log_data)
print("Extracted IPs:", ip_addresses)
