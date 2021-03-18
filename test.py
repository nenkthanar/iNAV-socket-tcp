from TCPClient import TCPClient
import time


app = TCPClient() # Create new class object
app.address = ('localhost',5000) # Set up ip and port for connection
app.start() # Start connection and running forever
time.sleep(5) # Delay 5 secs
app.send("test1") # Send message
time.sleep(2) # Delay 2 secs
print(app.rcvmsg)# Print out to see receive message
time.sleep(1) # Delay 2 secs
app.stop() # Stop running 
