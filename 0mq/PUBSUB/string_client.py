import zmq         # pkg load zeromq;
context=zmq.Context()
sock1=context.socket(zmq.SUB) # sock1=zmq_socket(ZMQ_SUB);
sock1.connect("tcp://127.0.0.1:5556");
sock1.setsockopt(zmq.SUBSCRIBE, b"")
vector1=[]
while (True):
  string_recv=sock1.recv()          # recv=zmq_recv(sock1, Nt*8*2/P, 0);
  print(string_recv.decode('ascii'))
