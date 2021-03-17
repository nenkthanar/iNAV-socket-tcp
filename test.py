from tcp import TCP
import time
from threading import Thread

app = TCP()
app.address = ('192.168.250.1',5000)
app.start()
time.sleep(5)
app.send("test1")
time.sleep(2)
app.stop()
