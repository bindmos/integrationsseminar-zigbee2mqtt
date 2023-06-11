from config import MQTT_HOST, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPIC, MQTT_QOS,TZ
from client import create_client, start_client
import time
from lifecycle_manager import GracefulKiller
from datetime import datetime as dt
import json

# This is the action that happens when a message in the topic arrives
def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    #print(str(TZ.localize(dt.now()))+" [Message recieved] (" + str(msg.topic) + "): " + str(data))
    json_data = json.loads(data) #{"battery":100,"humidity":49.81,"linkquality":113,"temperature":25.99,"voltage":3100}
    temperature_now = json_data["temperature"]
    humidity_now = json_data["humidity"]
    #Detect Temperature Changes
    global temperature_last
    if temperature_last != temperature_now:
        temperature_last = temperature_now
        print(str(TZ.localize(dt.now()))+" [Temperature] " +str(temperature_now) + "°C")
    #Detect Humidity Changes
    global humidity_last
    if humidity_last != humidity_now:
        humidity_last = humidity_now
        print(str(TZ.localize(dt.now()))+" [Humidity] " +str(humidity_now) + "%")   

if __name__ == '__main__':
    print("Temperature Subscriber")
    print(str(TZ.localize(dt.now())) + " Starting MQTT-Subscriber")
    mqtt_client = create_client(mqtt_username = MQTT_USERNAME, mqtt_password = MQTT_PASSWORD,mqtt_topic = MQTT_TOPIC,mqtt_qos = MQTT_QOS,on_message=on_message)
    start_client(mqtt_client, MQTT_HOST, MQTT_PORT)
    print(str(TZ.localize(dt.now())) + " MQTT-Subscriber started")
    killer = GracefulKiller()
    while not killer.kill_now:
        time.sleep(1)
    print(str(TZ.localize(dt.now())) + " Disconnecting from broker")
    mqtt_client.unsubscribe(MQTT_TOPIC)
    mqtt_client.disconnect()
    print("Goodbye")