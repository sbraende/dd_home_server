# Flask API for Temperature Data Transmission

This project implements a Flask API to transmit temperature data from a Raspberry Pi using a DHT11/DHT12/AM2302 sensor. The API provides temperature and humidity readings from the sensor, and it can be accessed by clients to retrieve the latest data.

## Features

- Retrieves temperature and humidity readings from a DHT11/DHT12/AM2302 sensor connected to a Raspberry Pi.
- Provides an API endpoint to fetch the latest temperature and humidity data.
- Supports configuration via a JSON file for room, host, port, sensor type, and sensor pin.

## Getting Started

1. Clone this repository to your Raspberry Pi.
2. Install the required Python packages using `pip`:

   ```bash
   pip install flask Adafruit_DHT
3. Rename config_template.json to config.json. Change the configuration parameters as needed. 
4. Run the flask server: 
   ```bash
   python3 app.py
5. Access the API endpoint to retrieve temperature and humidity data.

## API Endpoints
- `/data:` Retrieves the latest temperature and humidity readings.

## Dependencies
- Flask: A lightweight Python web framework.
- Adafruit_DHT: A Python library to interact with DHT sensors.