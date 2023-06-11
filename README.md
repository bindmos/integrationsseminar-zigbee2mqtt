# Temperature Subscriber

This MQTT Subscriber is subscribed to the topic "zigbee2mqtt/temperature-sensor"
When a Message from ZigBee2MQTT appears, the temperature data and the humidity data are written to console output.

A Message can look like this:

## MQTT-Subscriber

Recieve Temperature data from Zigbee Sensor via MQTT

### Installation

- Requirements: Docker, Docker-Compose
- Run Command `docker compose up -d --build`

### Access the Broker

The Broker is reachable under the following URL [localhost:1883](mqtt://localhost:1883)  
No Authentication necessary

### Content of directories

- broker: Basic Config File for Eclipse Mosquitto
- temperature_subscriber: Source code of this MQTT-Subscriber

### Technical details

- MQTT-Communication based on Eclipse paho library for python
- Packaged as Docker Container
