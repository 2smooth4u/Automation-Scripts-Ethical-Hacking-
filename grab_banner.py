# Import socket module for network connections
import socket 

# Import argparse module to handle command-line arguments
import argparse

# Function to grab the banner of a service running on a specific IP and port
def get_banner(ip, port):
    try: 
        # Create a socket object
        s = socket.socket()
        # Set timeout to 1 second for responsiveness
        s.settimeout(1)
        # Try to connect to the given IP and port
        s.connect((ip, port))
        # Receive up to 1024 bytes of data and decode it to string
        banner = s.recv(1024).decode().strip()
        return banner 
    except Exception as e:
        # Return None if connection fails or an error occurs
        return None
    finally:
        # Always close the socket to free resources
        s.close()

# Function to scan ports on the target IP and collect banners
def scan_ports(ip, start_port, end_port):
    banners = {}  # Dictionary to hold port:banner pairs
    for port in range(start_port, end_port + 1):
        banner = get_banner(ip, port)
        if banner:
            banners[port] = banner  # Store banner only if received
    return banners

# Main function to handle command-line arguments and output results
def main():
    # Set up argument parser with a description
    parser = argparse.ArgumentParser(description="Grab banner of running services for target IP")
    # Expect one positional argument: the IP address
    parser.add_argument("ip", type=str, help="IP address to scan")
    # Parse the arguments
    args = parser.parse_args()
    ip = args.ip
    # Scan all ports from 1 to 65535 for the given IP
    banners = scan_ports(ip, 1, 65535)
    # Print out ports and their corresponding banners
    print("Open ports with banners:")
    for port, banner in banners.items():
        print(f"Port {port} : {banner}") 

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
