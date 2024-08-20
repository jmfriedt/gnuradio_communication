import socket      # pkg load sockets;
import zmq         # pkg load zeromq;
import array
import matplotlib.pyplot as plt

Nt=1024
context=zmq.Context()
sock1=context.socket(zmq.REQ) 
sock1.connect("tcp://127.0.0.1:5556");
while True:
  noerror=1;
  while noerror:
    sock1.send(b"Hello")
    rcv=sock1.recv()
#    print(rcv.decode('ascii'))
    recv=array.array('i',rcv)
    print(f"{len(recv)} {recv[0]} {recv[1]} {recv[-1]}")
