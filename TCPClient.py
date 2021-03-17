import socket
import signal
import sys
from threading import Thread

class TCP():
    def __init__(self): 
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('0.0.0.0',5000)
        self.th = Thread(target=self.receive)

    def connect(self):
        self.sock.connect(self.address)
        print('connecting to =>',self.address)
        
    def send(self,message):
        msg = bytes(message,'utf-8')
        print('sending =>',message)
        self.sock.sendall(msg)

    def stop(self):
        print("disconnect")
        self.running = False
        self.sock.close()

    def receive(self):
        self.connect()
        while self.running:
            data = self.sock.recv(1024)
            if len(data) > 0:
                print('received <= ',data.decode('utf-8'))
            if self.running == False:
                break

    def start(self):
        self.th.start()
            
                



    