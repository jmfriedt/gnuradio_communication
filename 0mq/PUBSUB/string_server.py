import zmq         # pkg load zeromq;
import time

port = "5556"
payload="Hello "
context=zmq.Context()
sock=context.socket(zmq.PUB)
sock.bind("tcp://*:"+str(port)) # broadcast
k=0
while True:
    sock.send_string(payload+str(k))
    k=k+1
    time.sleep(1)
