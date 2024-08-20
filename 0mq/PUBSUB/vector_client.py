import numpy as np # pkg load signal;
import zmq         # pkg load zeromq;
import array
from matplotlib import pyplot as plt

Nt=256
context=zmq.Context()

sock1=context.socket(zmq.SUB) # sock1=zmq_socket(ZMQ_SUB);
sock1.connect("tcp://127.0.0.1:5556");
sock1.setsockopt(zmq.SUBSCRIBE, b"")
vector1=[]
while (len(vector1)<Nt):
  raw_recv=sock1.recv()         
#  recv=array.array('f',raw_recv)
  recv=array.array('i',raw_recv) 
  print(f"{recv[0]} {recv[1]} {recv[-1]}")
  plt.plot(recv)
  plt.show()
#    vector1tmp=recv[0::2]
#    vector2tmp=recv[1::2]
