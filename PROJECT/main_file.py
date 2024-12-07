import os
import time
import csv
import requests
from Adafruit_DHT import DHT11, read_retry
import bme280
import smbus2
from datetime import datetime

# Sensor IDs
sensor_ids = [371, 372, 374, 375, 378]

# Configuration
DHT11_PIN = 7  # GPIO pin where the DHT11 sensor is connected
CSV_FILE = "sensor_data.csv"
REMOTE_SERVER_URL = "192.168.4.137"

# Server and user details
server_ip = "192.168.4.137"
user = {'username': 'UNANDI', 'password': 'nananandi08'}

# Initialize BME280
def initialize_bme280():
    try:
        port = 1
        address = 0x76
        bus = smbus2.SMBus(port)
        bme280.load_calibration_params(bus, address)
        return bus, address
    except Exception as e:
        print(f"Error initializing BME280: {e}")
        return None, None

# Collect data from sensors
def collect_sensor_data(dht_pin, bme_bus, bme_address):
    try:
        # Read data from DHT11
        humidity_dht, temperature_dht = read_retry(DHT11, dht_pin)

        if humidity_dht is None or temperature_dht is None:
            raise ValueError("Failed to read data from DHT11 sensor.")

        # Read data from BME280
        bme_data = bme280.sample(bme_bus, bme_address)
        temperature_bme = bme_data.temperature
        humidity_bme = bme_data.humidity
        pressure = bme_data.pressure

        # Current datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "datetime": current_time,
            "temperature_dht": round(temperature_dht, 2),
            "humidity_dht": round(humidity_dht, 2),
            "temperature_bme": round(temperature_bme, 2),
            "humidity_bme": round(humidity_bme, 2),
            "pressure": round(pressure, 2)
        }
        return data
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
        login_response = requests.post(f'http://{server_ip}/login', json=user)
        cookie = login_response.json().get('access_token')
        if not cookie:
            raise ValueError("Failed to retrieve access token. Check login credentials.")

        auth = {'Authorization': f'Bearer {cookie}'}

        if 'datetime' not in data:
            raise ValueError("Data must include a 'datetime' key.")

        # Convert datetime to ISO 8601 format
        timestamp = datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
        formatted_datetime = timestamp.isoformat()

        data_dict = []
        for value in data.values():
            data_dict.append(value)

        for i in range(len(sensor_ids)):  # Ensure all sensor IDs are processed
            new_record = {
                "datetime": formatted_datetime,
                "sensor_id": sensor_ids[i],
                "value": data_dict[i+1],
            }
            response = requests.post(f'http://{server_ip}/reading/new', json=new_record, headers=auth)

            if response.status_code in [200, 201]:  # Treat both 200 and 201 as success
                print(f"Data uploaded successfully for sensor {sensor_ids[i]}.")
            else:
                print(f"Failed to upload data for sensor {sensor_ids[i]}. "
                      f"Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error uploading data: {e}")

# Main function
def main():
    bme_bus, bme_address = initialize_bme280()
    if not bme_bus or not bme_address:
        print("BME280 sensor initialization failed. Exiting.")
        return

    print("Starting data collection...")
    while True:
        data = collect_sensor_data(DHT11_PIN, bme_bus, bme_address)
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
