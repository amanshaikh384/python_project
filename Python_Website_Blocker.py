import platform
import os
import time

# List of distracting websites to block
blocked_websites = [
    "www.facebook.com",
    "www.twitter.com",
    "www.instagram.com",
    # Add more websites as needed
]

# Hosts file path for different operating systems
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    hosts_path = "/etc/hosts"
else:
    print("Unsupported operating system.")
    exit()

# Localhost IP address
localhost_ip = "127.0.0.1"

# Working hours (24-hour format)
start_hour = 9
end_hour = 17

def block_websites():
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in blocked_websites:
            if website not in content:
                file.write(f"{localhost_ip}\t{website}\n")

def unblock_websites():
    with open(hosts_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in blocked_websites):
                file.write(line)
        file.truncate()

if __name__ == "__main__":
    print("Python Website Blocker")
    while True:
        current_hour = time.localtime().tm_hour
        if 9 <= current_hour < 17:
            print("Blocking distracting websites...")
            block_websites()
        else:
            print("Unblocking distracting websites...")
            unblock_websites()
        
        # Check every 60 seconds (can be adjusted as needed)
        time.sleep(60)
