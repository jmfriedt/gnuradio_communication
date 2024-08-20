// gcc -lpaho-mqtt3c

#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include "MQTTClient.h"

#define ADDRESS     "tcp://127.0.0.1:1883"
#define CLIENTID    ""
#define TOPIC       "float_vect"
#define QOS         1
#define TIMEOUT     10000L
#define N 1024

int main(int argc, char* argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    MQTTClient_deliveryToken token;
    int rc;
    int32_t payload[N];
    int k;
    for (k=0;k<N;k++) payload[k]=k;

    MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;

    MQTTClient_connect(client, &conn_opts);
    pubmsg.payload = payload;
    pubmsg.payloadlen = sizeof(payload); // 4096
    pubmsg.qos = QOS;
    pubmsg.retained = 0;
    MQTTClient_publishMessage(client, TOPIC, &pubmsg, &token);
    printf("Waiting for up to %d seconds for publication\n",(int)(TIMEOUT/1000));
    rc = MQTTClient_waitForCompletion(client, token, TIMEOUT);
    printf("Message with delivery token %d delivered\n", token);
    MQTTClient_disconnect(client, 10000);
    MQTTClient_destroy(&client);
    return rc;
}
