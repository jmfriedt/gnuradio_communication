import numpy as np # pkg load signal;
import zmq         # pkg load zeromq;
import time

port = "5556"

context=zmq.Context()
sock=context.socket(zmq.PUB)
sock.bind("tcp://*:"+str(port)) # broadcast
k=0
while True:
    payload=np.arange(0+k,1024+k,dtype=np.int32)
    print(k)
    k=k+1
    sock.send(payload)
    time.sleep(1)
