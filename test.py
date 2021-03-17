from TCPClient import TCP
import time
from threading import Thread

app = TCP() # Create new class object
app.address = ('localhost',5000) # Set up ip and port for connection
app.start() # Start connection and running forever
time.sleep(5) # Delay 5 secs
app.send("test1") # Send message
print(app.rcvmsg)
time.sleep(2) 
print(app.rcvmsg)# Delay 2 secs
time.sleep(1) 
app.stop() # Stop running 
