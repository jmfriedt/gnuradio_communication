#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <zmq.h>

int main()
{   int k=0;
    char message[256];
    void *context = zmq_ctx_new();
    void *publisher = zmq_socket(context, ZMQ_PUB);
    if (zmq_bind(publisher, "tcp://127.0.0.1:5556")==0)
      {while (1)
       {sprintf(message,"Hello %03d",k);k++;
        zmq_send(publisher, message, strlen(message), 0);
        sleep(1);
       }
       zmq_close(publisher);
       zmq_ctx_destroy(context);
      }
    else printf("Socket error\n");
    return 0;
}
