import paho.mqtt.client as mqtt
import numpy

client=mqtt.Client()
client.connect("127.0.0.1")

data=numpy.arange(0,1024,dtype=numpy.int32)
client.publish("float_vect", data.tobytes() ,0)
# mosquitto_sub -t "float_vect"
