# Import the requests library to make HTTP requests
import requests

# Import sys to handle command-line arguments and exit
import sys

try:
    # Open and read the wordlist file containing possible subdomain names
    with open("/usr/share/wordlists/rockyou.txt", 'r', encoding='utf-8', errors='ignore') as file:
        sub_list = file.read()
except Exception as e:
    # Handle file-related errors (e.g., not found or permission denied)
    print("Error occurred : {e}")
    sys.exit(1)  # Exit if wordlist cannot be loaded

# Split the wordlist into individual subdomain names
subdoms = sub_list.splitlines()

# Iterate over each subdomain from the list
for sub in subdoms:
    # Construct full subdomain URL using the base domain passed as a command-line argument
    sub_domains = f"http://{sub}.{sys.argv[1]}"  # Example: http://test.example.com

    try:
        # Attempt to send an HTTP GET request to the subdomain
        requests.get(sub_domains)
    except requests.ConnectionError:
        # Ignore if the request fails (domain doesn't exist or no response)
        pass
    else:
        # If no exception, print that the subdomain is valid (it responded)
        print("Valid domain: ", sub_domains)
