from os import environ
from pytz import timezone

MQTT_HOST = environ.get('MQTT_HOST')
if not MQTT_HOST:
    raise ValueError("No MQTT_HOST set")

MQTT_PORT = int(str(environ.get('MQTT_PORT')))
if not MQTT_PORT:
    raise ValueError("No MQTT_PORT set")

MQTT_USERNAME = environ.get('MQTT_USERNAME')
if not MQTT_USERNAME:
    raise ValueError("No MQTT_USERNAME set")

MQTT_PASSWORD= environ.get('MQTT_PASSWORD')
if not MQTT_PASSWORD:
    raise ValueError("No MQTT_PASSWORD set")

MQTT_TOPIC= environ.get('MQTT_TOPIC')
if not MQTT_TOPIC:
    raise ValueError("No MQTT_TOPIC set")

MQTT_QOS= int(str(environ.get('MQTT_QOS')))
if not MQTT_QOS:
    MQTT_QOS = 0

TZ = environ.get('TZ')
if not TZ:
    TZ = "Etc/UTC"
TZ = timezone(TZ)