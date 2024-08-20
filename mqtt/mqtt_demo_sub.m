pkg load mqtt
client = mqttclient("tcp://127.0.0.1")
subs = subscribe(client, "float_vect")
vector=[]
do
  recv = read(client, "float_vect");
  if (isempty(recv)==0)
   % vector=typecast(recv,"single complex");
     vector=typecast(recv.Data,"int32")
  end
until (isempty(vector)==0)
