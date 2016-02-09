#initialize any zmq libs
import zmq
import time
#multiple contexts can be created in an app.
#contexts are thread-safe unlike sockets
context = zmq.Context()

#create socket from the context
socket = context.socket(zmq.REP)
