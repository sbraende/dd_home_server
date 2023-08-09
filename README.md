# Server side digital-twin setup for Raspberry Pi 

Using a Raspberry Pi with a DHT11, this program will log temperature and humidity data to a local sqlite database.

Requires:
- Raspberry Pi Raspberry OS connected with DHT11 sensor (hardcoded to GPIO datapin 17 at the moment).
- Adafruit_DHT python library. 

Install: 
- In terminal type: `sudo pip3 install Adafruit_DHT`
- In the config_db.py. Fill in the userdata fields on top of the document. Feel free to harcode the openweather_apikey or create a file in the project structure called "openweather_apikey.txt" and type in your personal api-key. You can get the api-key by regintering on https://openweathermap.org. 

Run:
- Start the program by running main.py. 