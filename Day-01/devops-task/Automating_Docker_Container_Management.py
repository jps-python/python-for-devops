import docker
client = docker.from_env()

# Pull and run a container
container = client.containers.run("nginx", detach=True, ports={"80/tcp": 8080})
print("Container Started:", container.id)
