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

socket.connect("tcp://localhost:%s" % port)
print 'bound server to port'

while True:
	msg = socket.recv()
	print msg
	socket.send('client message to server1')
	socket.send('client message to server2')
	time.sleep(1)

