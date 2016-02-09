# zeromq-pair-pattern
Talking Client and server code for PAIRed socked pattern

<h1>PAIR pattern with ZeroMQ and Python</h1>
<p>Pair patterns provide bidirectional sockets which can only connect to one peer at a time, without any state associated with the socket connection.</p>

To run start server first then client with same port:
python zmq-pair-server.py 5556 <br>
python zmq-pair-client.py 5556

