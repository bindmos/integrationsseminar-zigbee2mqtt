# Beispiel-Implementierung für Zigbee2MQTT

## Benötigte Hardware

- Zigbee-USB-Dongle "Zigbee CC2531 USB Dongle"
- Temperatur-Sensor "SONOFF SNZB-02"
- PC / Notebook

## Benötigte Software auf dem PC / Notebook

- Für MQTT-Broker und MQTT-Subscriber: Docker, Docker-Compose
- Für Zigbee2MQTT: Git, NodeJS 16

## Theoretischer Ablauf der Kommunikation

Kommunikationsprotokolle in Klammern

*"Von der Temperatur-Messung zum MQTT-Subscriber"*

        Temperatur-Sensor -> (Zigbee) -> Zigbee-USB-Dongle -> Anwendung Zigbee2MQTT -> (MQTT) -> Mosquitto-Broker -> (MQTT) -> Temperatur-Subscriber

# 1. Temperatur-Subscriber und MQTT-Broker

Der Temperatur-Subscriber abonniert das Topic "zigbee2mqtt/temperature-sensor" und wartet auf entsprechende Nachrichten des Temperatursensors. Wenn Temperatur- und Luftfeuchtigkeits-Messwerte empfangen werden, dann gibt die Anwendung diese auf der Kommandozeile aus. Außerdem wird ein lokaler Eclipse Mosquitto Broker gestartet, mit dem die Anwendung im Integrationsseminar genutzt wird.

## Installation

1. Docker und Docker-Compose müssen lokal installiert sein. Unter Windows ist auch Docker Desktop möglich.
2. Datei "docker-compose.yml"  
In der Datei "docker-compose.yml" sind über die Umgebungsvariablen Standardwerte definiert, mit denen Broker, Subscriber und die Zigbee2MQTT-Anwendung im Rahmen des Integrationsseminars betrieben wurden.
3. Broker und Subscriber starten  
Befehl im Hauptverzeichnis dieses Projekts ausführen  
`docker compose up -d --build`

    Zuerst wird das Docker-Image für den MQTT-Subscriber erstellt, anschließend werden Broker und Subscriber gestartet.

## Inhalt der Verzeichnisse

- broker: Grundlegende Konfigurationsdatei für Eclipse Mosquitto
- temperature-subscriber: Python-Code des MQTT-Subscribers

    ### Kurzbeschreibung der enthaltenen Python-Files

    - app.py: Anwendung initialisieren  
    - client.py: Kommunikation mit dem Broker 
    - config.py: Umgebungsvariablen zur Konfiguration einlesen
    - lifecycle_manager.py: SIGINT oder SIGTERM-Signale für einen geregelten Abmeldeprozess vom Broker anwenden   

# 2. Zigbee2MQTT

Schnittstelle zwischen Zigbee-Geräten und MQTT-Anwendungen
Sendet mit dem USB-Dongle "Zigbee CC2531 USB Dongle" per Zigbee empfangene Daten an einen definierten MQTT-Broker

Im Integrationsseminar wurden beispielhaft Temperatur- und Luftfeuchtigkeitsmesswerte des Sensors *SONOFF SNZB-02* unter dem Topic "zigbee2mqtt/temperature-sensor" an den Broker übertragen.

## Hinweis

Zigbee2MQTT konnte nicht in Docker auf Windows (Windows Subsystem for Linux / kurz: WSL) realisiert werden, da WSL2 aktuell (2023-06-14) keine Kommunikation über Serielle Ports zulässt. Vielleicht ist es durch künftige Entwicklungen möglich, eine etwas "schlankere" Implementierung auszuführen, die ausschließlich auf Containern basiert.  
Link zur Diskussion: [https://github.com/microsoft/WSL/issues/4322](https://github.com/microsoft/WSL/issues/4322)

## Benötigte Software auf dem PC / Notebook

- Git
- NodeJS 16

## Installation (Im Rahmen der Abgabe bereits enthalten)

Es folgt das Protokoll der durchlaufenen Schritte für evtl. Reproduktion. Im eingereichten Quellcode sind die Schritte bereits ausgeführt.

1. Git und NodeJS 16 müssen lokal installiert sein. Das USB-Dongle muss in einen freien USB-Slot am PC gesteckt werden und betriebsbereit sein. Eine Treiberinstallation sollte nicht notwendig sein.
2. Kommandozeile öffnen und in diesen Ordner navigieren
3. Quellcode für Zigbee2MQTT von GitHub laden  
Befehl  
`git clone --depth 1 git@github.com:Koenkk/zigbee2mqtt.git zigbee2mqtt`
4. Abhängigkeiten von Zigbee2MQTT herunterladen  
Befehle  

    1. `cd zigbee2mqtt`
    2. `npm ci`

5. Konfiguration  
Zugangsdaten MQTT-Broker und COM-Port definieren
Hierfür die Datei `"data/configuration.yaml"` bearbeiten und die entsprechenden Abschnitte in der Datei anpassen oder ergänzen, wenn nicht vorhanden.

    ### Zugangsdaten MQTT-Broker

        mqtt:
            base_topic: zigbee2mqtt # Gibt den Präfix des Topics aller MQTT-Nachrichten vor, die verschickt werden
            server: mqtt://localhost:1883 # mqtts:// für TLS-Verschlüsselte Verbindungen; 1883 ist der Port des Brokers
            user: username_here # Nutzername beim Broker
            password: superstrong_password_here # Passwort beim Broker

    ### Definition COM-Port

    Zunächst muss im Windows Geräte-Manager der COM-Port ermittelt werden, der dem USB-Dongle zugewiesen wurde. Hier im Beispiel ist dies "COM5"

        serial:
            port: \\.\COM5

    ### Beispiel einer minimalen, funktionsfähigen Konfigurationsdatei

        mqtt:
            base_topic: zigbee2mqtt
            server: mqtt://localhost:1883
            user: zigbee-usb
            password: tigbee-password
        serial:
            port: \\.\COM5

6. Start  
Befehl: `npm start`

    Wenn der in der Konfigurationsdatei definiere Broker nicht erreicht werden kann, stürzt die Anwendung an dieser Stelle ab. Um fortzufahren, müssen je nach Fehlermeldung der Broker gestartet oder die Zugangsdaten überprüft werden.

7. Zigbee-Geräte mit USB-Dongle und Zigbee2MQTT verbinden  
Unterschiede je nach Gerät. Beispiele für die im Integrationsseminar genutzten Geräte:  

    - [Temperatursensor SONOFF SNZB-02](https://www.zigbee2mqtt.io/devices/SNZB-02.html)
    - [Bewegungsmelder SONOFF SNZB-03](https://www.zigbee2mqtt.io/devices/SNZB-03.html)

    ### Automatische Änderungen an der Konfigurationsdatei 

    Es wird nach dem Anlernen automatisch ein neuer Abschnitt hinzugefügt.
    Dieser enthält als wesentliche Komponenten eine Geräte-ID des Zigbee-Geräts.
    
    
    Zusätzlich lässt sich über das Attribut "friendly_name" das Topic festlegen, unter dem die Daten des Gerätes an den Broker weitergereicht werden. 
    Dieses Attibut muss evtl manuell hinzugefügt werden. Im folgenden Beispiel soll vom MQTT-Subscriber später das Topic "zigbee2mqtt/temperature-sensor" genutzt werden:

        devices:
        '0x00124b0029195ebb': # Geräte-ID
            friendly_name: 'temperature-sensor' # Selbst definierter Teil des gemeinsamen MQTT-Topics


8. Web UI / Frontend  
Wenn folgende Zeilen in der Konfigurationsdatei ergänzt werden, kann eine Visualisierung der Zigbee2MQTT-Anwendung im Browser unter der Adresse [localhost:8080](http://localhost:8080) erreicht werden.  

        frontend:
            port: 8080
            host: 0.0.0.0
            homeassistant: false
            permit_join: true

## Weiterführende Dokumentation

Unter der folgenden URL ist die vollständige Dokumentation mit Hinweisen zu Konfiguration und Nutzung der Library auffindbar: [Zigbee2MQTT Dokumentation](https://www.zigbee2mqtt.io/guide/getting-started/)