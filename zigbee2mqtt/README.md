# Zigbee2MQTT

## Zweck

Schnittstelle zwischen Zigbee-Geräten und MQTT-Anwendungen
Sendet per Zigbee empfangene Daten an einen definierten MQTT-Broker

## Installation

1. Git und NodeJS 16 müssen lokal installiert sein
2. Quellcode für Zigbee2MQTT von GitHub laden  
Befehl: `git clone --depth 1 git@github.com:Koenkk/zigbee2mqtt.git`
3. Abhängigkeiten von Zigbee2MQTT herunterladen  
Befehle  

    - `cd src`
    - `npm ci`

4. Konfiguration  
Zugangsdaten MQTT-Broker und COM-Port definieren
Datei "data/configuration.yaml"

### Abschnitt für Zugangsdaten MQTT-Broker

    mqtt:
        base_topic: zigbee2mqtt # Das gibt den Präfix des Topics aller MQTT-Nachrichten vor, die verschickt werden
        server: mqtt://localhost:1883 # mqtts:// für TLS-Verschlüsselte Verbindungen
        user: username_here # Nutzername beim Broker
        password: superstrong_password_here # Passwort beim Broker

### Abschnitt für Definition COM-Port

Zunächst muss im Windows Geräte-Manager der COM-Port ermittelt werden, der dem USB-Dongle zugewiesen wurde. Hier im Beispiel ist dies "COM5"

    serial:
        port: \\.\COM5

5. Start  
Befehl: `npm start`

6. Zigbee-Geräte in der Anwendung anlernen  
Unterschiede je nach Gerät. Beispiele für die im Integrationsseminar genutzten Geräte:  

    - [Temperatursensor](https://www.zigbee2mqtt.io/devices/SNZB-02.html)
    - [Bewegungsmelder](https://www.zigbee2mqtt.io/devices/SNZB-03.html)

7. Web UI / Frontend
Erreichbar unter [localhost:8080](http://localhost:8080)

## Weiterführende Dokumentation

Zu finden unter der folgenden URL [Zigbee2MQTT Dokumentation](https://www.zigbee2mqtt.io/guide/getting-started/)