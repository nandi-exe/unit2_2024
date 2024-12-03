```.py
import os
import time
import csv
import requests
from Adafruit_DHT import DHT11, read_retry
from bmp280 import BMP280  # Install library via `pip install bmp280`
from datetime import datetime

# Configuration
DHT11_PIN = 4  # GPIO pin where the DHT11 sensor is connected
CSV_FILE = "sensor_data.csv"
REMOTE_SERVER_URL = "http://192.168.4.137/readings"

# Initialize BMP280
def initialize_bmp280():
    try:
        bmp_sensor = BMP280()
        return bmp_sensor
    except Exception as e:
        print(f"Error initializing BMP280: {e}")
        return None

# Collect data from sensors
def collect_sensor_data(dht_pin, bmp_sensor):
    try:
        # Read data from DHT11
        humidity, temperature = read_retry(DHT11, dht_pin)
        
        # Read data from BMP280
        pressure = bmp_sensor.get_pressure() if bmp_sensor else None
        
        # Current datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "datetime": current_time,
            "temperature": round(temperature, 2) if temperature else None,
            "humidity": round(humidity, 2) if humidity else None,
            "pressure": round(pressure, 2) if pressure else None
        }
    except Exception as e:
        print(f"Error collecting sensor data: {e}")
        return None

# Save data to CSV
def save_to_csv(data, file_path):
    try:
        file_exists = os.path.exists(file_path)
        with open(file_path, mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Upload data to remote server
def upload_to_server(data):
    try:
        response = requests.post(REMOTE_SERVER_URL, json=data)
        if response.status_code == 200:
            print("Data uploaded successfully.")
        else:
            print(f"Failed to upload data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error uploading data: {e}")

# Main function
def main():
    bmp_sensor = initialize_bmp280()
    if not bmp_sensor:
        print("BMP280 sensor initialization failed. Exiting.")
        return
    
    print("Starting data collection...")
    while True:
        data = collect_sensor_data(DHT11_PIN, bmp_sensor)
        if data:
            print(f"Collected Data: {data}")
            save_to_csv(data, CSV_FILE)
            upload_to_server(data)
        else:
            print("Failed to collect sensor data.")
        
        # Wait for the next minute
        time.sleep(60)

# Run the script
if __name__ == "__main__":
    main()
```

import os
import time
import csv
import requests
from Adafruit_DHT import DHT11, read_retry
from bmp280 import BMP280  # Install library via `pip install bmp280`
from datetime import datetime

# Configuration
DHT11_PIN = 4  # pin where the DHT11 is
CSV_FILE = "sensor_data.csv"
REMOTE_SERVER_URL = "http://192.168.4.137/readings"

# initialize
def initialize_bmp280():
    try:
        bmp_sensor = BMP280()
        return bmp_sensor
    except Exception as e:
        print(f"fail")
        return None

# Collect data from sensors
def collect_sensor_data(dht_pin, bmp_sensor):
    try:
        # Read DHT11 sensor
        humidity, temperature = read_retry(DHT11, dht_pin)
        
        # Read BMP280 sensor
        pressure = bmp_sensor.get_pressure() if bmp_sensor else None
        
        # Current datetime
        datetime= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "datetime": datetime,
            "temperature": round(temperature, 2) if temperature else None,
            "humidity": round(humidity, 2) if humidity else None,
            "pressure": round(pressure, 2) if pressure else None
        }
    except Exception as e:
        print(f"Error")
        return None

# Save data to CSV
def save_to_csv(data, file_path):
    file_exists = os.path.exists(file_path)
    with open(file_path, mode="a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# Upload data to remote server
def upload_to_server(data):
    try:
        response = requests.post(REMOTE_SERVER_URL, json=data)
        print(f"Data uploaded")
    except Exception as e:
        print(f"Error uploading")

# Main function
def main():
    bmp_sensor = initialize_bmp280()
    if not bmp_sensor:
        print("BMP280 failed")
        return
    
    print("Starting data collection...")
    for i in range(2880):
    data = collect_sensor_data(DHT11_PIN, bmp_sensor)
    if data:
        print(f"Collected Data: {data}")
        save_to_csv(data, CSV_FILE)
        upload_to_server(data)
    else:
        print(f"Failed to collect data at iteration {i + 1}")

    # Wait for the next minute
    time.sleep(60)

main()

