# Import required libraries
import sys              # Used to flush output
import socket           # Provides network socket interface
import pyfiglet         # Used to display ASCII banner

# Create and print an ASCII banner
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

# Define the target IP address to scan
ip = '192.168.17.133'

# List to store open ports
open_ports = []

# Define the port range to scan (1 to 65534)
ports = range(1, 65535)

# Function to check if a specific port is open
def probe_port(ip, port, result=1):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for each port probe to 0.5 seconds
        sock.settimeout(0.5)
        # Attempt to connect to the target port
        r = sock.connect_ex((ip, port))  # Returns 0 if connection is successful
        if r == 0:
            result = r  # Port is open
        socket.close()  # ⚠️ Incorrect: should be sock.close()
    except Exception as e:
        # Ignore exceptions (e.g., connection errors)
        pass
    return result

# Loop through all ports and check which are open
for port in ports:
    sys.stdout.flush()  # Ensure clean terminal output
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

# Display the result
if open_ports:
    print("Target open ports are:")
    print(sorted(open_ports))
else:
    print("No ports are open")
