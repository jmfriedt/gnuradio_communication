# voir https://opensource.com/article/18/6/mqtt

import paho.mqtt.client as mqtt
import numpy
import time

def callback_func(client, userdata, message):
    print("rcv ", numpy.frombuffer(message.payload, dtype=numpy.float64)) # pour recevoir de Octave
    # print("rcv ", numpy.frombuffer(message.payload, dtype=numpy.int32))

client=mqtt.Client()
client.connect("127.0.0.1")

client.subscribe("float_vect")
client.on_message=callback_func
client.loop_start() 
time.sleep(40)
