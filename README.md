# Firetv Basic Stick
This is to setup Alexa <-> Homeassistant <-> FireTV Basic Stick 

## Steps

1. Activate debug mode (ADB) in your firetv stick.
2. Run install.sh in your homeassistant hub.
3. Set your FireTV IP address in /usr/local/bin/firetv-rest-server.py
4. Run gunicorn (the REST server)
5. Add scripts.yaml contents to your scripts.yaml file in homeassistant
6. Add configuration.yaml contents to your configuration.yaml file in homeassistant

WIP:

7. Upload amazon labmda function
8. Create custom skill
