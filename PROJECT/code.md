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

