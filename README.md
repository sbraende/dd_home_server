# Server side digital-twin setup for Raspberry Pi 

Using a Raspberry Pi with a DHT11, this program will log temperature and humidity data to a local sqlite database.

Requires:
- Raspberry Pi Raspberry OS connected with DHT11 sensor (hardcoded to GPIO datapin 17 at the moment).
- Adafruit_DHT python library. 

Install: 
- In terminal type: `sudo pip3 install Adafruit_DHT`
- Create a file called room_id.txt in the main project structure. Write the name of the room you are using the sensor/raspberry. 
- Create a file called openweather_apikey.txt in the main project structure. Write down your api key from openweather.

Run:
- Start the program by running main.py