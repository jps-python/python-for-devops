import os

def check_server(host):
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    if response == 0:
        print(f"{host} is UP")
    else:
        print(f"{host} is DOWN")

# Example usage
check_server("google.com")
