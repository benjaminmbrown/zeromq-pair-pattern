#initialize any zmq libs
import zmq
print zmq.pyzmq_version()
import time
import sys
import time

port = "5556"

#multiple contexts can be created in an app.
#contexts are thread-safe unlike sockets
context = zmq.Context()

#create socket from the context
socket = context.socket(zmq.PAIR)
#bind socket to port
socket.bind("tcp://*:%s" % port)

while True:
	socket.send("Server message to client3")
	msg= socket.recv()
	print msg
	time.sleep(1)
