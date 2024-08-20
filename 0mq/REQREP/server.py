import numpy as np # pkg load signal;
import zmq         # pkg load zeromq;
import time

port = "5556"

# payload=np.arange(0,1023)
payload="Hello "
k=0
context=zmq.Context()
while True:
  sock=context.socket(zmq.REP)
  sock.bind("tcp://*:"+str(port)) # broadcast
  while True:
    message = sock.recv()
    print(message)
    payload=np.arange(0+k,1024+k,dtype=np.int32)
    sock.send(payload)
    print(k)
    k=k+1
    time.sleep(1)
