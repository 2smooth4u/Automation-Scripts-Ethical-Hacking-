# Import all modules from scapy (used for packet crafting and sniffing)
from scapy.all import *

# Define the network interface to use for sending packets (e.g., eth0)
interface = "eth0"

# Define the IP range to scan using ARP (CIDR notation for a /24 subnet)
ip_range = "192.168.17.0/24"

# Define the broadcast MAC address (used to broadcast ARP requests)
broadcastMac = "ff:ff:ff:ff:ff:ff"

# Craft an Ethernet packet with destination set to broadcast MAC
# and stack it with an ARP request for the target IP range
packet = Ether(dst=broadcastMac)/ARP(pdst=ip_range)

# Send the packet and receive responses:
# - srp() sends and receives Ethernet frames at Layer 2
# - timeout=2 seconds wait per packet
# - iface specifies which interface to use
# - inter=0.1 sets delay between each packet
ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

# Loop through each received response
for send, receive in ans:
    # Print the MAC and IP address of each host that responded
    print(receive.sprintf(r"%Ether.src% - %ARP.src%"))
