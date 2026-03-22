pkg load zeromq;
Nt=2*1024
sock1=zmq_socket(ZMQ_SUB);
zmq_connect(sock1,"tcp://127.0.0.1:5556");
zmq_setsockopt(sock1, ZMQ_SUBSCRIBE, "");
do
  recv=zmq_recv(sock1, Nt*8, 0);
% vector=typecast(recv,"single complex");
  vector=typecast(recv,"int32");
  plot(vector)
  refresh()
  printf("%d %d %d\n",vector(1), vector(2),vector(end))
until (1==0)
