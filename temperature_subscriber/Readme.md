# status-subscriber

app.py: Initializing the application  
client.py: Functionality to communicate with an MQTT-Broker  
config.py: Read Environment Variables
lifecycle_manager.py: Keep track of SIGINT or SIGTERM in order to gracefully disconnect from the MQTT Broker  
api_connector.py: Functionality for converting MQTT-Messages to JSON and sending to the REST-API  
