# MQTT communication

MQTT is a star-shaped communication scheme where a unique broker (MQTT server) 
collects all requests, whether incoming or outgoing. This MQTT broker is provided
with the ``mosquitto`` package under GNU Linux, whose capability is tested using
``mosquitto_sub`` and ``mosquitto_pub`` of the ``mosquitto-clients`` package.

In these examples, we assume the broker is running on the localhost, port 1883 (default).
