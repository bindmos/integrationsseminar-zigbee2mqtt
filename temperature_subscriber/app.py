from config import MQTT_HOST, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPIC, MQTT_QOS,TZ
from client import create_client, start_client
import time
from lifecycle_manager import GracefulKiller
from datetime import datetime as dt

if __name__ == '__main__':
    print("Temperature Subscriber")
    print(str(TZ.localize(dt.now())) + " Starting MQTT-Subscriber")
    mqtt_client = create_client(mqtt_username = MQTT_USERNAME, mqtt_password = MQTT_PASSWORD,mqtt_topic = MQTT_TOPIC,mqtt_qos = MQTT_QOS)
    start_client(mqtt_client, MQTT_HOST, MQTT_PORT)
    print(str(TZ.localize(dt.now())) + " MQTT-Subscriber started")
    killer = GracefulKiller()
    while not killer.kill_now:
        time.sleep(1)
    print(str(TZ.localize(dt.now())) + " Disconnecting from broker")
    mqtt_client.unsubscribe(MQTT_TOPIC)
    mqtt_client.disconnect()
    print("Goodbye")