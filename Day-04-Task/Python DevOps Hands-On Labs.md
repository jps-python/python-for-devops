Let's go with **hands-on labs** for Python in DevOps! 🚀 I'll guide you through practical exercises covering automation, infrastructure as code (IaC), CI/CD, and monitoring/logging.  

## **🔹 Python DevOps Hands-On Labs**  
### **🛠 Lab 1: Automating Server Health Checks (Linux/Windows)**
📌 *Goal*: Write a Python script to check if a server is up and log the results.

#### **🔹 Steps:**
1️⃣ Install Python (if not already installed).  
2️⃣ Create a script to ping a server and log the status.  
3️⃣ Run the script and check logs.  

#### **🔹 Code:**
```python
import os
import logging

# Configure logging
logging.basicConfig(filename="server_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def check_server(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    status = "UP" if response == 0 else "DOWN"
    logging.info(f"Server {host} is {status}")
    print(f"Server {host} is {status}")

# Example usage
check_server("google.com")
```

#### **🔹 Run the Script:**
```sh
python3 server_health.py
```
✅ *Check `server_health.log` for server status logs!*

---

### **🛠 Lab 2: Deploy an AWS EC2 Instance with Python**
📌 *Goal*: Use **Boto3** to automate AWS infrastructure creation.

#### **🔹 Steps:**
1️⃣ Install `boto3`:  
   ```sh
   pip install boto3
   ```
2️⃣ Configure AWS CLI:  
   ```sh
   aws configure
   ```
3️⃣ Run the Python script to launch an EC2 instance.

#### **🔹 Code:**
```python
import boto3

ec2 = boto3.resource('ec2')

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-12345678',  # Replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

print("EC2 Instance Launched:", instance[0].id)
```

✅ *Run this script to create an AWS instance!*

---

### **🛠 Lab 3: Docker Container Management with Python**
📌 *Goal*: Use **Docker-Py** to automate container operations.

#### **🔹 Steps:**
1️⃣ Install Docker and `docker-py`:  
   ```sh
   pip install docker
   ```
2️⃣ Pull an image and start a container using Python.

#### **🔹 Code:**
```python
import docker

client = docker.from_env()

# Pull and run a container
container = client.containers.run("nginx", detach=True, ports={"80/tcp": 8080})

print("Started Nginx Container:", container.id)
```

✅ *Check running containers with `docker ps`.*

---

### **🛠 Lab 4: Automate Jenkins Job Triggering**
📌 *Goal*: Use Python to trigger a **Jenkins build**.

#### **🔹 Steps:**
1️⃣ Install `jenkinsapi`:  
   ```sh
   pip install jenkinsapi
   ```
2️⃣ Run the script to trigger a Jenkins job.

#### **🔹 Code:**
```python
from jenkinsapi.jenkins import Jenkins

jenkins_url = "http://localhost:8080"
server = Jenkins(jenkins_url, username="admin", password="password")

# Trigger a job
job_name = "Deploy-App"
server.build_job(job_name)
print(f"Triggered Jenkins job: {job_name}")
```

✅ *Watch the Jenkins job execution in real-time!*

---

### **🛠 Lab 5: Monitoring with Prometheus and Python**
📌 *Goal*: Send **custom metrics** to Prometheus using Python.

#### **🔹 Steps:**
1️⃣ Install `prometheus-client`:  
   ```sh
   pip install prometheus-client
   ```
2️⃣ Run a simple metrics exporter.

#### **🔹 Code:**
```python
from prometheus_client import start_http_server, Counter
import random
import time

REQUEST_COUNT = Counter("app_requests_total", "Total app requests")

def process_request():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    start_http_server(8000)  # Expose metrics on port 8000
    while True:
        process_request()
```

✅ *Visit `http://localhost:8000/metrics` to see Prometheus data!*

---

### **Next Steps**
Do you want to:  
🔹 Explore **Terraform + Python** for IaC?  
🔹 Deep dive into **Python-based logging with Splunk/ELK**?  
🔹 Automate **CI/CD pipelines with Python + GitHub Actions**?  

Let me know your focus, and I’ll tailor the next labs! 🚀