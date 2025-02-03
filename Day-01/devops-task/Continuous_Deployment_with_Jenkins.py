from jenkinsapi.jenkins import Jenkins

jenkins_url = "http://localhost:8080"
server = Jenkins(jenkins_url, username="admin", password="password")

# Trigger a Jenkins job
job_name = "Deploy-App"
server.build_job(job_name)
print(f"Triggered Jenkins job: {job_name}")
