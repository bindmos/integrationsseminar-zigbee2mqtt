import paho.mqtt.client as paho
import ssl
import json
from json.decoder import JSONDecodeError
import sys
from datetime import datetime as dt
from config import TZ
import uuid

last_temperature = 0

# Setup the client with credentials, topic, quality of service
def create_client(mqtt_username, mqtt_password, mqtt_topic, mqtt_qos, version='3',mytransport='tcp'):
    clientid = uuid.uuid1
    clientid = str(clientid)  
    if version != '5' and version != '3':
        raise ValueError("MQTT Version must be 3 or 5")

    if version == '5':
        client = paho.Client(client_id=clientid,
                            transport=mytransport,
                            protocol=paho.MQTTv5)
        
        def on_connect(client, userdata, flags, reasonCode, properties):
            connect(client, reasonCode, mqtt_qos, mqtt_topic)
        
        def on_disconnect(client, userdata, reasonCode, properties):
            disconnect(client, reasonCode)
        
        def on_subscribe(client, userdata, mid, reasonCodes, properties):
            print(str(TZ.localize(dt.now())) + " [Subscribe] to topic '" +str(mqtt_topic) + "' "+str(mid)+" "+str(reasonCodes))

    if version == '3':
        client = paho.Client(client_id=clientid,
                            transport=mytransport,
                            protocol=paho.MQTTv311,
                            clean_session=True)
       
        def on_connect(client, userdata, flags, reasonCode):
            connect(client, reasonCode, mqtt_qos, mqtt_topic)
        
        def on_disconnect(client, userdata,rc):
            disconnect(client, rc)
        
        def on_subscribe(client, userdata, mid, granted_qos):
            print(str(TZ.localize(dt.now()))+ " [Subscribe] to topic '" +str(mqtt_topic) + "' "+str(mid)+" "+str(granted_qos))
    
    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLS, ciphers=None)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.username_pw_set(mqtt_username, mqtt_password)
    return client

# This is the action that happens when a message in the topic arrives
def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    #print(str(TZ.localize(dt.now()))+" [Message recieved] (" + str(msg.topic) + "): " + str(data))
    json_data = json.loads(data) #{"battery":100,"humidity":49.81,"linkquality":113,"temperature":25.99,"voltage":3100}
    temperature_now = json_data["temperature"]
    #Detect Temperature Changes
    if temperature_now != last_temperature:
        print(str(TZ.localize(dt.now()))+" [Temperature] " +str(temperature_now) + "°C")       

# Connect to the Broker
def start_client(client, mqtt_host, mqtt_port):
    client.connect(host=mqtt_host, port=mqtt_port, keepalive=60)
    client.loop_start()

# Print start of connections and send topic to broker
def connect(client,reasonCode,qos,topic):
    print(str(TZ.localize(dt.now()))+" [Connect] result code "+str(reasonCode))
    client.subscribe(topic, qos=qos)

# Print end of connection
def disconnect(client, reasonCode):
    print(str(TZ.localize(dt.now()))+" [Disconnect] result code "+str(reasonCode))
    client.loop_stop()