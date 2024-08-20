pkg load mqtt
client = mqttclient("tcp://127.0.0.1")
vector=[1:1024]
data=typecast(vector,"char")
write(client, "float_vect", data, "QualityOfService", 1);
