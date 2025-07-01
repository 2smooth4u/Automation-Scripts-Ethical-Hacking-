import socket 
import argparse


def get_banner (ip,port):

      try: 
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        banner=s.recv(1024).decode().strip()
        return banner 
      except Exception as e:
        return None
      finally:
        s.close()


def scan_ports(ip, start_port, end_port):
      banners = {}
      for port in range(start_port,end_port+1):
        banner = get_banner(ip, port)
        if banner:
          banners[port] = banner
         
      return banners

def main() :
     parser = argparse.ArgumentParser(description="Grab banner of running services for target IP")
     parser.add_argument("ip" , type=str, help="IP address to scan")
     args = parser.parse_args()
     ip = args.ip
     banners = scan_ports(ip, 1, 65535)
     print("Open ports with banners:")
     for port, banner in banners.items():
       print(f"Port {port} : {banner}") 

if __name__ == "__main__":
         main()
