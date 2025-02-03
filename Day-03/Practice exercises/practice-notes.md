### **Using Variables to Store and Manipulate Configuration Data in a DevOps Context with Python**

In **DevOps**, managing configuration data efficiently is crucial for automation, deployment, and monitoring. Python provides multiple ways to store, manipulate, and use configuration data dynamically across different environments.

---

## **1. Using Environment Variables in Python**
Environment variables are widely used in DevOps for storing sensitive information like API keys, database credentials, and service endpoints.

### **1.1. Setting Environment Variables**
- **Linux/macOS:**
  ```bash
  export DB_HOST="prod-db.example.com"
  export DB_USER="admin"
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:DB_HOST = "prod-db.example.com"
  $env:DB_USER = "admin"
  ```

### **1.2. Accessing Environment Variables in Python**
```python
import os

db_host = os.getenv("DB_HOST", "localhost")  # Default to localhost if not set
db_user = os.getenv("DB_USER", "root")

print(f"Database Host: {db_host}")
print(f"Database User: {db_user}")
```

**Best Practice:** Use **dotenv** to manage environment variables.
```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db_host = os.getenv("DB_HOST")
print(f"Database Host: {db_host}")
```

---

## **2. Using Configuration Files in Python**
Configuration files (JSON, YAML, INI) are commonly used in DevOps pipelines and tools.

### **2.1. JSON Configuration File**
```json
{
    "database": {
        "host": "prod-db.example.com",
        "user": "admin",
        "password": "securepassword"
    }
}
```
#### **Reading JSON in Python**
```python
import json

with open("config.json") as config_file:
    config = json.load(config_file)

db_host = config["database"]["host"]
print(f"Database Host: {db_host}")
```

---

### **2.2. YAML Configuration File**
```yaml
database:
  host: prod-db.example.com
  user: admin
  password: securepassword
```
#### **Reading YAML in Python**
```python
import yaml

with open("config.yaml") as file:
    config = yaml.safe_load(file)

db_host = config["database"]["host"]
print(f"Database Host: {db_host}")
```
```bash
pip install pyyaml
```

---

### **2.3. INI Configuration File**
```ini
[database]
host = prod-db.example.com
user = admin
password = securepassword
```
#### **Reading INI in Python**
```python
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

db_host = config["database"]["host"]
print(f"Database Host: {db_host}")
```

---

## **3. Using Python for Configuration Management in DevOps**
Python can dynamically modify and apply configurations in **CI/CD pipelines, cloud infrastructure, and containerized environments**.

### **3.1. Modifying Configurations Dynamically**
Example: **Modify JSON configuration before deployment**
```python
import json

# Load config
with open("config.json") as file:
    config = json.load(file)

# Modify database host dynamically
config["database"]["host"] = "new-db.example.com"

# Save the modified config
with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("Updated Configuration:", config)
```

---

### **3.2. Using Python for CI/CD Pipeline Configuration**
Python can integrate with **Jenkins, GitHub Actions, and GitLab CI/CD**.

#### **Example: Using Python to Read and Modify Environment Variables in a Jenkins Pipeline**
```groovy
pipeline {
    agent any
    environment {
        DB_HOST = "prod-db.example.com"
        DB_USER = "admin"
    }
    stages {
        stage('Deploy') {
            steps {
                script {
                    def db_host = sh(script: "python3 get_config.py DB_HOST", returnStdout: true).trim()
                    echo "Deploying to ${db_host}"
                }
            }
        }
    }
}
```

Python script (`get_config.py`):
```python
import os
import sys

key = sys.argv[1]
value = os.getenv(key, "not found")
print(value)
```

---

## **4. Storing Configuration in Kubernetes ConfigMaps**
**ConfigMaps** store environment-specific configurations in Kubernetes.

### **4.1. Define a Kubernetes ConfigMap**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DB_HOST: "prod-db.example.com"
```
### **4.2. Access ConfigMap in a Kubernetes Pod**
```yaml
envFrom:
  - configMapRef:
      name: app-config
```

### **4.3. Read Kubernetes ConfigMap in Python**
```python
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

config_map = v1.read_namespaced_config_map("app-config", "default")
print("Database Host:", config_map.data["DB_HOST"])
```

```bash
pip install kubernetes
```

---

## **5. Infrastructure as Code (IaC) with Python**
Python can generate and manipulate configurations dynamically for **Terraform, Ansible, and Docker**.

### **5.1. Terraform Configuration with Python**
```python
import hcl  # HashiCorp Configuration Language parser
with open("main.tf", "r") as file:
    terraform_config = hcl.load(file)

print(terraform_config)
```

---

## **6. Best Practices for Using Configuration Variables in DevOps**
1. **Use Environment Variables for Secrets**  
   - Avoid storing sensitive information in config files.
   - Use **HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault**.

2. **Version Control Configuration Files**  
   - Store YAML/JSON files in **Git repositories**.
   - Use **CI/CD pipelines** to apply configurations dynamically.

3. **Use Configuration Management Tools**  
   - **Ansible, Terraform, and Kubernetes ConfigMaps** for managing dynamic configurations.

4. **Use Feature Flags for Dynamic Configurations**  
   - Use **LaunchDarkly, Unleash, and Flipper** to enable or disable features dynamically.

5. **Validate Configuration Before Deployment**  
   - Use schema validation tools like **JSON Schema** or **YAML Lint**.

---

## **7. Tools for Configuration Management in DevOps**
| **Tool**          | **Purpose**                                      |
|-------------------|--------------------------------------------------|
| **Ansible**      | Automates configuration management & deployment.  |
| **Terraform**    | Infrastructure as Code (IaC) for cloud providers. |
| **Kubernetes**   | Manages containerized application configurations. |
| **Jenkins**      | Uses environment variables for pipeline settings. |
| **Vault**        | Securely manages secrets and credentials.         |
| **Consul**       | Service discovery and configuration management.   |

---

## **8. Conclusion**
- **Python is a powerful tool** for managing configuration data in DevOps.
- **Use environment variables, JSON/YAML files, and ConfigMaps** to store configuration.
- **Modify configurations dynamically using Python scripts** for automation.
- **Leverage Kubernetes, Terraform, and Ansible** for large-scale infrastructure management.

Would you like a **hands-on tutorial** for a specific tool like Ansible, Kubernetes, or Terraform? 🚀