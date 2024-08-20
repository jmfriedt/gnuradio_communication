// https://stackoverflow.com/questions/67025151/zeromq-pub-sub-example-in-c-libzmq

#include <stdio.h>
#include <zmq.h>

int main()
{
    void *context = zmq_ctx_new();
    void *subscriber = zmq_socket(context, ZMQ_SUB);
    char message[256];
    int len;
    zmq_connect(subscriber, "tcp://127.0.0.1:5556");
    while (1) {
        len=zmq_recv(subscriber, message, 12, 0);
        if (len!=-1) {message[len]=0; printf("%s\n", message);}
        else printf("error\n");
    }
    zmq_close(subscriber);
    zmq_ctx_destroy(context);
    return 0;
}
