// https://stackoverflow.com/questions/67025151/zeromq-pub-sub-example-in-c-libzmq

#include <stdio.h>
#include <zmq.h>
#include <stdint.h>

int main()
{   int32_t *res;
    void *context = zmq_ctx_new();
    void *subscriber = zmq_socket(context, ZMQ_SUB);
    char message[1024*4];
    int len;
    zmq_connect(subscriber, "tcp://127.0.0.1:5556");
    zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, "", 0);
    res=(int32_t*)(message);
    while (1) {
        len=zmq_recv(subscriber, message, 1024*4, 0);
        if (len!=-1) {printf("%d: %ld %ld %ld\n",len,(res[0]),res[1],(res[1023]));}
        else printf("error\n");
    }
    zmq_close(subscriber);
    zmq_ctx_destroy(context);
    return 0;
}
