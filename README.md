# Server side digital-twin setup for Raspberry Pi 

Using a Raspberry Pi with a DHT11, this program will log temperature and humidity data to a local sqlite database.

Requires:
- Raspberry Pi Raspberry OS connected with DHT11 sensor.
- Adafruit_DHT python library. 

Install: 
- In terminal type: `sudo pip3 install Adafruit_DHT`
- Create a file called room_id.txt in the main project structure. Write the name of the room you are using the sensor/raspberry. 

Run:
- Start the program by running main.py