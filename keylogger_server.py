import socket 

def start_server(ip,port):
  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.bind((ip,port))
  server.listen(5)
  print(f"Server is listening on {ip}:{port}")

    while True: 
       client_socket, addr = server.accept()
       print(f"Connection from {addr}")
       data =  client_socket.recv(1024).decode()
       if data:
          print(f"Received data : {data}")
       client_socket.close()

if __name__ == "__main__":
      start_server("0.0.0.0", 1234)
