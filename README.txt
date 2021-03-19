*********Create by thanarnop Robkwaen*************
  **** How to test running *** 
1 Run command : python TCPServer.py
2 Run command : python test.py 


*** Discription for example in file test.py ***
We create this project to use with local robot controler for easy using of compact code of using socket tcp

from TCPClient import TCP        # =  Import class TCPClient 

app = TCPClient()                # =  Create new class object

app.address = ('localhost',5000) # =  Set up ip and port for connection

app.start()                      # =  Start connection and running forever

time.sleep(5)                    # =  Delay 5 secs

app.send("test1")                # =  Test send message then server will echo back message store in buffer virable  rcvmsg

print(app.rcvmsg)                # =  Use print command to display receive value

time.sleep(1)                    # =  Delay 2 secs

app.stop()                       # =  Test stop running method in class if not stop application will run forever

