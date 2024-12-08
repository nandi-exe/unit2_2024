# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

### Problem Definition
Our client, Mr. X, a boarding student at a local international school, is an avid coffee collector who values the rich aroma and flavor of premium coffee beans. However, he has grown increasingly concerned about the potential impact of humidity on the quality of his carefully curated collection. Fluctuating humidity levels in his pantry may lead to issues such as moisture absorption, mold growth, or a loss of freshness, all of which can compromise the beans' quality. Mr. X has already encountered some problems with declining bean quality. Ensuring the optimal storage conditions for his coffee has become a priority for Mr. X as he strives to preserve the distinct characteristics of his beans.

### Proposed Solution

To address the client’s requirements, a cost-effective and scalable solution includes a low-cost sensing device for humidity and temperature, combined with a custom data processing script for analyzing the acquired samples. For the sensing device, an excellent choice is the DHT11 [[1]](https://www.adafruit.com/product/386) [[2]](https://www.researchgate.net/publication/366522967_An_Approach_for_Implementing_Innovative_Weather_Monitoring_System_with_DHT11_Sensor_and_Arduino_Uno_Tool_based_on_IoT) [[3]](https://www.researchgate.net/publication/350859817_Automatic_Room_Temperature_Control_System_Using_Arduino_UNO_R3_and_DHT11_Sensor) sensor, which is available for less than $5 and provides adequate precision and range for the application (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). While alternatives like the DHT22, AHT20, or AM2301B offer higher specifications, the DHT11’s simplicity, using SPI communication instead of more complex protocols like I2C, makes it a better fit for this application.

To interface the DHT11 sensor with a computational platform, we proposed using a Raspberry Pi instead of an Arduino. The Raspberry Pi, starting at around $10 for the Raspberry Pi Zero, is a versatile, low-cost computer [[4]](https://ijece.iaescore.com/index.php/IJECE/article/view/27879) that includes GPIO pins for direct sensor interfacing and runs a full operating system. Unlike the Arduino, which requires an additional computer to run the data processing software, the Raspberry Pi can both collect data and run the required Python scripts, consolidating the hardware into a single device. Its flexibility and computing power also make it easier to integrate additional functionalities, such as remote monitoring or cloud storage, should the client’s needs evolve.

Considering the budgetary constraints and system requirements, the proposed software tool for this solution is Python. Python's open-source nature, platform independence, and extensive library support [[5]](https://www.nature.com/articles/s41592-019-0686-2) [[6]](https://www.python.org/doc/essays/blurb/) make it ideal for data analysis and visualization tasks. The language’s high abstraction level simplifies development and maintenance compared to lower-level alternatives like C or C++ [[7]](https://realpython.com/python-vs-cpp/#memory-management). Python’s automatic memory management and vast ecosystem of libraries ensure efficient development and seamless scalability for future enhancements [[8]](https://github.com/tino/pyFirmata) [[9]](https://pythongeeks.org/advantages-disadvantages-of-python/). By leveraging Python on a Raspberry Pi, the system achieves a balance of simplicity, cost-effectiveness, and flexibility to meet the client’s needs.

### Design Statement
To address Mr. X's concerns about the impact of fluctuating humidity on his coffee bean collection, we aim to design a cost-effective and user-friendly system that monitors and maintains optimal storage conditions. The system will leverage the DHT11 sensor for temperature and humidity measurements, integrated with a Raspberry Pi for data collection and processing. Python will be employed for data analysis, visualization, and potential predictive modeling. The solution will include a local storage system for continuous monitoring and a scalable framework for future enhancements, such as remote data access or cloud integration. This system will ensure precise and reliable tracking of environmental conditions, empowering Mr. X to preserve the quality and freshness of his premium coffee beans effectively.

### Success Criteria
1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. [Issue tackled]: Helps Mr. X monitor and evaluate storage conditions over time to identify environmental factors impacting coffee bean quality.
2. [HL] The local variables will be measured using a set of 3 sensors around the dormitory.
[Issue tackled]: Ensures comprehensive and accurate data collection by covering multiple points within the dormitory, addressing variations in environmental conditions.
3. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations. (SL: linear model), (HL: non-linear model)
[Issue tackled]: Enables Mr. X to understand trends and relationships between variables, aiding in optimizing storage conditions through predictive insights.
4. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standard deviation, minimum, maximum, and median.
[Issue tackled]: Allows Mr. X to assess variability and stability of environmental conditions, crucial for maintaining premium coffee bean quality.
5. (SL)The Local samples are stored in a csv file and (HL) posted to the remote server as a backup. 
[Issue tackled]: Provides reliable data storage and backup to prevent loss of critical information, ensuring continuous monitoring.
6. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL).
[Issue tackled]: Assists Mr. X in preemptive action against potential environmental changes that could harm his coffee bean collection.
7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure (HL). 
[Issue tackled]: Offers a clear and accessible summary of findings and helpful recommendations, empowering Mr. X to implement effective storage strategies.

---

## Criteria B: Design
### System Diagrams

![systemdiagram](https://github.com/user-attachments/assets/dba28917-4f10-44b0-898e-e894d8960afa)
Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables were measured locally with a network of DHT11/BMP280 sensors on a Raspberry Pi. A remote server provides an API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

### Flow Diagram 1
![image](https://github.com/user-attachments/assets/c4886776-946e-4fa2-8f90-9ce32af0a45c)
Fig 1.1: Sensor registration code, specifically DHT Temperature.
### Flow Diagram 2
![image](https://github.com/user-attachments/assets/af8eda74-9a3a-46e0-b612-4b913ffbdccb)

Fig 1.2: Code for saving data to csv.

### Flow Diagram 3
![image](https://github.com/user-attachments/assets/8c95ecbe-df9c-4ce2-a2ef-bdda07354d5e)
Fig 1.3: Code for uploading data to server.

Both Fig 1.2 and 1.3 include logging in at every iteration, because the login token would expire after 15 iterations, so we decided to add that step to every upload (explained more in Criteria C, commented code) just to play it safe.

### How is the data stored and managed?
The collected data is stored locally in a CSV file for structured access and offline analysis. This format allows for easy reading, modification, and integration with data-processing tools. To ensure data persistence and accessibility, the CSV data is periodically uploaded to an API server. This two-tiered approach balances local storage for quick access with remote storage for backup and broader analysis, providing a reliable and scalable system for managing the collected environmental data.

### Record of Tasks
| Task No | Planned Action                                | Planned Outcome                                                    | Time Estimate | Target Completion Date | Criteria   |
|---------|----------------------------------------------|----------------------------------------------------------------------|---------------|-------------------------|------------|
| 1       | Write problem definition, design statement, and success criteria | Finalize problem definition, design statement, and criteria for evaluation | 15 mins      | Nov 16                 | A, B       |
| 2       | Research sensors and purpose of local and remote measurements | Identify sensors needed and their purpose for data collection          | 30 mins      | Nov 17                 | A          |
| 3       | Create GitHub repository, fork Dr Ruben's template | Centralize project files, including system diagrams, code, and data     | 10 mins      | Nov 17                 | B          |
| 4       | Set up Raspberry Pi for sensor data collection | Collect temperature, humidity, and pressure data locally               | 1 hour       | Nov 19                 | C          |
| 5       | Develop modular functions for sensor data collection | Modularize code for handling data from each sensor                     | 3 hours      | Nov 21                 | C          |
| 6       | Program Raspberry Pi to integrate and collect data | Enable data collection from DHT11 and BME280 sensors                   | 1 hour       | Nov 23                 | C          |
| 7       | Test connections between sensors             | Ensure accurate data flow between sensors and Raspberry Pi            | 45 mins      | Nov 25                 | C          |
| 8       | Test sensor placement and data accuracy      | Verify sensor setup and accurate collection of temperature, humidity, pressure | 30 mins | Nov 25 | C, B |
| 9       | Save local data in CSV format                | Store data in a structured format for analysis                        | 1 hour       | Nov 27                 | C, SL      |
| 10      | Automate data collection                     | Schedule data collection every minute for continuous logging          | 1 hour       | Nov 27                 | C          |
| 11      | Automate uploading local data to remote server | Back up local data on a remote server                                | 30 mins      | Nov 29                 | C, HL      |
| 12      | Develop mathematical models for data         | Create models for temperature, humidity, and pressure data            | 3 hours      | Nov 30                 | HL         |
| 13      | Analyze local and remote data                | Compare key statistics (mean, median, range, etc.) for data           | 2 hours      | Dec 1                  | HL         |
| 14      | Predict future trends                        | Use past data to model 12-hour forecasts for environmental parameters | 2 hours      | Dec 2                  | HL         |
| 15      | Create graphs to visualize data              | Plot data trends for temperature, humidity, and pressure              | 3 hours      | Dec 2                  | C, HL      |
| 16      | Refine data visualizations                   | Improve clarity and design of graphs with labels and trends           | 2 hours      | Dec 4                  | C          |
| 17      | Draw code flow diagrams                      | Represent the code structure and logic visually                       | 1 hour       | Dec 5                  | B          |
| 18      | Draft scientific poster                      | Summarize data, models, and recommendations on a poster               | 2 hours      | Dec 5                  | D          |
| 19      | Plan video presentation outline              | Structure the content for the project video                           | 20 mins      | Dec 5                  | D          |
| 20      | Complete final documentation                 | Compile project documentation, including code and analysis            | 1 hour       | Dec 6                  | A, B, C    |
| 21      | Finalize scientific poster                   | Include refined graphs and conclusions summarizing the investigation  | 4 hours      | Dec 7                  | D          |
| 22      | Record and edit project video                | Create a video summarizing the solution, analysis, and poster         | 2 hours      | Dec 7                  | D          |
---

### Test Plan
| **Test Type**         | **Target**                                                                                  | **Procedure**                                                                                                                                                                                                                   | **Expected Outcome**                                                                                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect sensors & power        | Connect BME280 and DHT11 sensors to Raspberry Pi.                                          | **BME280:**<br>VIN - 3.3V or 5V (2C1R)<br>GND - GND (2C3R)<br>SCL - GPIO 3 (1C2R)<br>SDA - GPIO 2 (1C3R)<br><br>**DHT11:**<br>VCC - 3.3V (1C1R)<br>GND - GND (1C4R)<br>DATA - GPIO (1C5R)<br> Connect the micro-USB cable to the charging brick and a power source                                          | Sensors should be securely connected to the Raspberry Pi, ready for data collection.                                                                                      |
| Connect to Raspberry Pi| Access Raspberry Pi desktop remotely using VNC Viewer.                                     | Open VNC Viewer.<br>Type in the Raspberry Pi’s IP address.<br>Enter username: **MIKEANDUNANDI** and password: **ANYTHINGMEMORABLE123**.                                                                                      | The desktop of the Raspberry Pi should be displayed.                                                                                                                       |
| Run main.py            | Connect to the server and collect sensor data.                                             | Open the terminal and type the following commands line by line:<br>`python3 -m venv venv`<br>`source venv/bin/activate`<br>`python3 main.py`<br>Every minute, the terminal should display the data collected and verification messages. | A message displaying data from each sensor should pop up on the terminal every minute, along with verification statements.                                                 |
| Obtain sensor data     | Retrieve and display collected sensor data from the server.                                | Open PyCharm.<br>Run `data_retrieval.py`.                                                                                                                                                                                      | The program should produce lists showcasing the data collected by each sensor individually.                                                                                |
| Model the data         | Create graphs of collected and predicted data.                                             | Open PyCharm.<br>Run `extract_data.py`.                                                                                                                                                                                          | The program should produce 6 graphs:<br>- 2 for Temperature<br>- 2 for Humidity<br>- 2 for Pressure (collected and predicted).                                             |
| Produce statistics     | Calculate and display minimum, maximum, and average values for each sensor.                | Open PyCharm.<br>Run `statistics.py`.                                                                                                                                                                                          | The program should produce the minimum, maximum, and average values for each sensor.                                                                                      |


## Criteria C: Development

### List of techniques used
#### Core Techniques
1. Moving average for filtering noisy signals from sensors(with for loops inside)
Used to smooth sensor data and enhance model accuracy.
2. Data visualization
Visualizing trends and patterns in collected data for analysis.
3. Connecting to server using API
Establishing communication between the client and server for data exchange.
4. Data models
Implementing mathematical models for prediction and analysis.
5. File reading and modification
Handling CSV files for storing and accessing sensor data.
6. Registering and Login into API
Managing user authentication and token-based access.
7. Transmission of data to API servers
Sending serialized sensor data to a remote server.
8. Accessing API data and readings
Fetching stored data for local use and further analysis.
#### Programming Constructs
1. Functions
2. Lists and Dictionaries
3. For loop
4. While loop
5. Try-except statement
6. If-else conditional statement
#### Libraries
1. os
For interacting with the operating system, e.g., file paths.
2. time
For delays and timestamp-related operations.
3. csv
Reading from and writing to CSV files for structured data storage.
4. requests
Making HTTP requests for API interactions.
5. Adafruit - DHT11
Accessing temperature and humidity readings from the DHT11 sensor.
6. bme280
Reading temperature, humidity, and pressure from the BME280 sensor.
7. smbus2
Reading temperature, humidity, and pressure from the BME280 sensor.
8. datetime
Managing date and time information for data logging.
9. matplotlib
Creating graphs and visualizations for data analysis.
10. numpy
Performing numerical computations and data manipulation.

### Data Collection and Sorting: Success Criteria 1 & 3 (Remote part)
Server sensors can sometimes experience downtime or inconsistencies, leading to missing or irregular readings. To ensure data accuracy and reliability, we must identify a continuous 48-hour period (2880 readings) where data is complete and consistent. Steps 3, 4, and 5 allow us to filter out unreliable data and focus on analyzing high-quality, uninterrupted information based on previous sensor readings.

#### Code Breakdown
**Part 1: Data Collection and Organization
Step 1: Fetch Data from Server**
```.py
import requests
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from datetime import datetime

# Define the server IP to fetch data from
server_ip = "192.168.4.137"  # Server IP

# Send a GET request to fetch sensor readings
response = requests.get(f"http://{server_ip}/readings")

# Parse JSON response into Python dictionary
data = response.json()
readings = data["readings"][0]
```
**What it does: Sends a request to the server to fetch JSON data. The first set of readings is extracted for further processing.
Step 2: Organize Data by Sensor Type**
```.py
# Initialize lists for different sensor types
temperature_data = []
humidity_data = []
pressure_data = []

# Loop through each reading and separate by sensor type
for r in readings:
    timestamp = datetime.fromisoformat(r["datetime"])  # Convert ISO timestamp to datetime
    if r["sensor_id"] == 11:  # Temperature sensor
        temperature_data.append((timestamp, r["value"]))
    elif r["sensor_id"] == 10:  # Humidity sensor
        humidity_data.append((timestamp, r["value"]))
    elif r["sensor_id"] == 12:  # Pressure sensor
        pressure_data.append((timestamp, r["value"]))
```
**Purpose: Classifies sensor readings (temperature, humidity, pressure) into separate lists, tagging each reading with its timestamp.
****Step 3: Sort Data Chronologically**
```.py
# Sort readings for each sensor type by timestamp
temperature_data.sort(key=lambda x: x[0])
humidity_data.sort(key=lambda x: x[0])
pressure_data.sort(key=lambda x: x[0])
```
**Why: Time-series data needs to be in order for accurate analysis and modeling.
Step 4: Ensure Consecutive Data Quality**
```.py
# Minimum required readings for 48 hours (1 reading per minute)
min_required = 2880

def find_last_consecutive(data, required_count):
    """
    Finds the last block of consecutive readings of the required count.
    Ensures each reading is exactly 1 minute apart.
    """
    for i in range(len(data) - required_count, -1, -1):
        timestamps_block = [data[j][0] for j in range(i, i + required_count)]
        # Check if all timestamps are 1 minute apart
        if all((timestamps_block[j + 1] - timestamps_block[j]).seconds == 60 for j in range(len(timestamps_block) - 1)):
            return data[i : i + required_count]
    return []
```
**Why: Validates data integrity by ensuring each block of readings has no gaps.
Step 5: Apply Consecutive Check**
```.py
# Extract last block of 2880 consecutive readings for each sensor
temperature_consecutive = find_last_consecutive(temperature_data, min_required)
humidity_consecutive = find_last_consecutive(humidity_data, min_required)
pressure_consecutive = find_last_consecutive(pressure_data, min_required)

# Handle insufficient data
if not temperature_consecutive or not humidity_consecutive or not pressure_consecutive:
    print("Error: Not enough consecutive data for one or more sensors.")
    exit()
```
**What it does: Ensures all sensors have enough valid data for analysis.
Step 6: Extract and Separate Values**
```.py
# Extract timestamps and sensor values from consecutive readings
timestamps = [t[0] for t in temperature_consecutive]
temperatures = [t[1] for t in temperature_consecutive]
humidities = [h[1] for h in humidity_consecutive]
pressures = [p[1] for p in pressure_consecutive]
```
**Purpose: Prepares time-series data for modeling by separating timestamps and sensor values.
**#### Part 2: Mathematical Modeling and Visualization
**Step 1: Convert Time to Minutes**
**
```.py
# Convert timestamps to "minutes since start"
start_time = timestamps[0]
time_minutes = [(t - start_time).total_seconds() / 60 for t in timestamps]
```
**Why: Simplifies time representation for fitting mathematical models.
Step 2: Define Models**
```.py
def sine_model(x, A, B, C, D):
    """Sine function for periodic data (e.g., temperature, humidity)."""
    return A * np.sin(B * x + C) + D

def poly_model(x, a, b, c):
    """Quadratic polynomial for non-periodic data (e.g., pressure)."""
    return a * x**2 + b * x + c
```
**Models Used:
Sine: Captures periodic fluctuations (e.g., day-night temperature cycles).
Polynomial: Models trends in non-periodic data (e.g., pressure).
Step 3: Fit Models to Data**
```.py
# Fit models to sensor data
temp_params, _ = curve_fit(sine_model, time_minutes, temperatures, p0=[3, 0.003, 0, 26])
humidity_params, _ = curve_fit(sine_model, time_minutes, humidities, p0=[2, 0.003, 0, 16])
pressure_params, _ = curve_fit(poly_model, time_minutes, pressures)
```
**What it does: Finds optimal parameters for each model using curve fitting.
Step 4: Generate Predictions**
```.py
# Generate predictions using the fitted models
time_fit = np.linspace(0, max(time_minutes), 1000)  # Smoother time points
temp_fit = sine_model(time_fit, *temp_params)
humidity_fit = sine_model(time_fit, *humidity_params)
pressure_fit = poly_model(time_fit, *pressure_params)
```
**Why: Creates smooth curves for visual comparison against raw data.
Step 5: Plot Data and Models**
```.py
plt.figure(figsize=(12, 10))

# Temperature plot
plt.subplot(3, 1, 1)
plt.plot(time_minutes, temperatures, color="red", label="Data")
plt.plot(time_fit, temp_fit, color="blue", label="Sine Model Fit")
plt.title("Temperature Model")
plt.legend()
plt.grid()

# Humidity plot
plt.subplot(3, 1, 2)
plt.plot(time_minutes, humidities, color="blue", label="Data")
plt.plot(time_fit, humidity_fit, color="green", label="Sine Model Fit")
plt.title("Humidity Model")
plt.legend()
plt.grid()

# Pressure plot
plt.subplot(3, 1, 3)
plt.plot(time_minutes, pressures, color="green", label="Data")
plt.plot(time_fit, pressure_fit, color="purple", label="Polynomial Model Fit")
plt.title("Pressure Model")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
```
**What it does: Visualizes raw data and fitted models in subplots for comparison.

Conclusion**
This script ensures data integrity, fits appropriate models to sensor readings, and visualizes the data effectively. 

### Main code inside Raspberry Pi: Success criteria 2 & 5
```.py
# Import necessary libraries
import os  # For file operations
import time  # For delay operations
import csv  # For writing data to CSV files
import requests  # For making HTTP requests to the server
from Adafruit_DHT import DHT11, read_retry  # For reading data from the DHT11 sensor
import bme280  # For interfacing with the BME280 sensor
import smbus2  # For communication with I2C devices (used by BME280)
from datetime import datetime  # For working with dates and times

# Sensor IDs to differentiate sensor data
sensor_ids = [371, 372, 374, 375, 378]

# Configuration
DHT11_PIN = 7  # GPIO pin where the DHT11 sensor is connected
CSV_FILE = "sensor_data.csv"  # File to save sensor data locally
REMOTE_SERVER_URL = "192.168.4.137"  # Server's IP address

# Server and user details for authentication
server_ip = "192.168.4.137"
user = {'username': 'UNANDI', 'password': 'nananandi08'}

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



# Function to save sensor data to a CSV file
def save_to_csv(data, file_path):
    """
    Save sensor data to a CSV file.
    """
    try:
        # Check if the file already exists
        file_exists = os.path.exists(file_path)
        with open(file_path, mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()  # Write header only for new files
            writer.writerow(data)  # Write the data
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Function to upload sensor data to the remote server
def upload_to_server(data):
    """
    Upload sensor data to the remote server.
    Note: Login token expires after 15 uploads, so re-login is performed before every upload.
    """
    try:
        # Log in to the server
        login_response = requests.post(f'http://{server_ip}/login', json=user)
        cookie = login_response.json().get('access_token')
        if not cookie:
            raise ValueError("Failed to retrieve access token. Check login credentials.")

        auth = {'Authorization': f'Bearer {cookie}'}
        
        # Ensure data contains a valid datetime
        if 'datetime' not in data:
            raise ValueError("Data must include a 'datetime' key.")

        # Validate and format the datetime
        try:
            timestamp = datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
            formatted_datetime = timestamp.isoformat()
        except ValueError:
            raise ValueError(f"Invalid datetime format in data: {data['datetime']}")

        # Prepare data for each sensor
        data_dict = list(data.values())  # Convert data values to a list
        for i in range(len(sensor_ids)):
            new_record = {
                "datetime": formatted_datetime,
                "sensor_id": sensor_ids[i],
                "value": data_dict[i + 1]  # Skip 'datetime'
            }
            # Upload the record to the server
            response = requests.post(f'http://{server_ip}/reading/new', json=new_record, headers=auth)

            # Check upload status
            if response.status_code in [200, 201]:
                print(f"Data uploaded successfully for sensor {sensor_ids[i]}.")
            else:
                print(f"Failed to upload data for sensor {sensor_ids[i]}. "
                      f"Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error uploading data: {e}")

# Main function to run the script
def main():
    """
    Main function to initialize sensors, collect data, save to CSV, and upload to server.
    """
    # Initialize BME280 sensor
    bme_bus, bme_address = initialize_bme280()
    if not bme_bus or not bme_address:
        print("BME280 sensor initialization failed. Exiting.")
        return
    
    print("Starting data collection...")
    while True:
        # Collect sensor data
        data = collect_sensor_data(DHT11_PIN, bme_bus, bme_address)
        if data:
            print(f"Collected Data: {data}")
            save_to_csv(data, CSV_FILE)  # Save to CSV
            upload_to_server(data)  # Upload to server
        else:
            print("Failed to collect sensor data.")
        
        # Wait for the next minute before collecting data again
        time.sleep(60)

# Run the script
if __name__ == "__main__":
    main()
```

### Data Collection and Sorting (Local part): Success criteria 1
```.py
# Import necessary library
import matplotlib.pyplot as plt  # Used for creating plots and visualizing data

# Sensor data lists, each containing a series of recorded values (example data is shown)
# Replace these ellipses with actual sensor readings
BME_Temp = [22.8, 22.1, ...]  # BME280 sensor temperature readings (in degrees Celsius)
BME_Pressure = [1008.2, 1007.6, ...]  # BME280 sensor pressure readings (in hPa)
BME_Humidity = [45.2, 46.8, ...]  # BME280 sensor humidity readings (in percentage)
DHT_Temp = [23.1, 22.5, ...]  # DHT11 sensor temperature readings (in degrees Celsius)
DHT_Humidity = [47.3, 48.1, ...]  # DHT11 sensor humidity readings (in percentage)

# Extract the last 2880 values from each dataset
# This assumes the dataset contains values over a continuous interval (e.g., minutes, hours, etc.)
recent_temp_bme = BME_Temp[-2880:]  # Latest 2880 temperature readings from BME280
recent_hum_bme = BME_Humidity[-2880:]  # Latest 2880 humidity readings from BME280
recent_hpa_bme = BME_Pressure[-2880:]  # Latest 2880 pressure readings from BME280
recent_temp_dht = DHT_Temp[-2880:]  # Latest 2880 temperature readings from DHT11
recent_hum_dht = DHT_Humidity[-2880:]  # Latest 2880 humidity readings from DHT11

# Create a figure with multiple subplots to display sensor data
plt.figure(figsize=(12, 10))  # Set the overall figure size (width, height in inches)

# 1. Plot BME280 Temperature
plt.subplot(3, 2, 1)  # Create subplot in a 3x2 grid, position 1
plt.tight_layout()  # Automatically adjust subplot parameters for better layout
plt.plot(recent_temp_bme, label="BME Temperature", color="blue")  # Line plot for BME280 temperature
plt.title("BME280 Temperature")  # Title of the plot
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Temperature (C)")  # Y-axis label
plt.legend()  # Display legend for the plot
plt.grid(True)  # Add a grid for better readability

# 2. Plot BME280 Humidity
plt.subplot(3, 2, 2)  # Create subplot in a 3x2 grid, position 2
plt.tight_layout()  # Adjust layout
plt.plot(recent_hum_bme, label="BME Humidity", color="green")  # Line plot for BME280 humidity
plt.title("BME280 Humidity")  # Title of the plot
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Humidity (%)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# 3. Plot BME280 Pressure
plt.subplot(3, 2, 3)  # Create subplot in a 3x2 grid, position 3
plt.tight_layout()  # Adjust layout
plt.plot(recent_hpa_bme, label="BME Pressure", color="purple")  # Line plot for BME280 pressure
plt.title("BME280 Pressure")  # Title of the plot
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Pressure (hPa)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# 4. Plot DHT11 Temperature
plt.subplot(3, 2, 4)  # Create subplot in a 3x2 grid, position 4
plt.tight_layout()  # Adjust layout
plt.plot(recent_temp_dht, label="DHT Temperature", color="orange")  # Line plot for DHT11 temperature
plt.title("DHT11 Temperature")  # Title of the plot
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Temperature (C)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# 5. Plot DHT11 Humidity
plt.subplot(3, 2, 5)  # Create subplot in a 3x2 grid, position 5
plt.tight_layout()  # Adjust layout
plt.plot(recent_hum_dht, label="DHT Humidity", color="red")  # Line plot for DHT11 humidity
plt.title("DHT11 Humidity")  # Title of the plot
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Humidity (%)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# Create a new figure for sensor comparison plots
plt.figure(figsize=(12, 6))  # Set the size of the comparison figure

# 6. Temperature Comparison: BME280 vs. DHT11
plt.subplot(2, 1, 1)  # Create subplot in a 2x1 grid, position 1
plt.plot(recent_temp_bme, label="BME Temperature", color="blue")  # BME280 temperature plot
plt.plot(recent_temp_dht, label="DHT Temperature", color="orange", linestyle="--")  # DHT11 temperature plot (dashed line)
plt.title("Temperature Comparison: BME280 vs. DHT11")  # Title for comparison
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Temperature (C)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# 7. Humidity Comparison: BME280 vs. DHT11
plt.subplot(2, 1, 2)  # Create subplot in a 2x1 grid, position 2
plt.plot(recent_hum_bme, label="BME Humidity", color="green")  # BME280 humidity plot
plt.plot(recent_hum_dht, label="DHT Humidity", color="red", linestyle="--")  # DHT11 humidity plot (dashed line)
plt.title("Humidity Comparison: BME280 vs. DHT11")  # Title for comparison
plt.xlabel("Time (intervals)")  # X-axis label
plt.ylabel("Humidity (%)")  # Y-axis label
plt.legend()  # Display legend
plt.grid(True)  # Add a grid

# Adjust the layout of the comparison figure for better spacing
plt.tight_layout()  # Adjust subplot spacing
plt.show()  # Display all the plots
```
<img width="1197" alt="Screenshot 2024-12-09 at 7 22 54" src="https://github.com/user-attachments/assets/7ede14b4-331d-47a7-811d-460fae3555c2">
<img width="1201" alt="Screenshot 2024-12-09 at 7 23 27" src="https://github.com/user-attachments/assets/8dc56434-f799-487c-8d1a-7512bf3705ab">


### Statistical Analysis of Sensor Data: Success Criteria 3

Upon the collection of all the sensor data, we developed a function that calculated and collected statistical information, comprising of the mean, maximum, minimum and standard deviation.

```
def analyze_sensor_data(sensor_data):

    if not sensor_data:
        return {"mean": None, "std_dev": None, "min": None, "max": None}

    # Calculate mean
    total = sum(sensor_data)
    count = len(sensor_data)
    mean = round(total / count,2)

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in sensor_data) / (count - 1) if count > 1 else 0
    std_dev = round(variance ** 0.5,4)

    # Find min and max
    min_value = min(sensor_data)
    max_value = max(sensor_data)

    # Return results in a dictionary
    return {"mean": mean, "std_dev": std_dev, "min": min_value, "max": max_value}

# Usage
results_bme_temp = analyze_sensor_data(BME_Temp)
results_bme_hum = analyze_sensor_data(BME_Hum)
results_bme_hpa = analyze_sensor_data(BME_Pressure)
results_dht_temp = analyze_sensor_data(DHT_Temp)
results_dht_hum = analyze_sensor_data(DHT_Hum)

#Output
print("BME Temp ",results_bme_temp)
print("BME Humidity ",results_bme_hum)
print("BME Pressure ",results_bme_hpa)
print("DHT Temperature ",results_dht_temp)
print("DHT Humidity ",results_dht_hum)
```

Once collected, we used the figures found to summarize out findings in a table

| Sensor Name     | Sensor ID | Mean   | Maximum | Minimum | Standard Deviation |
|-----------------|-----------|--------|---------|---------|--------------------|
| BME Temperature | 374       | 22.75  | 28.65   | 21.7    | 0.5818             |
| BME Humidity    | 375       | 34.15  | 47.89   | 28.56   | 2.33               |
| BME Pressure    | 378       | 882.16 | 884.84  | 879.53  | 1.3401             |
| DHT Temperature | 371       | 22.83  | 28.5    | 21.0    | 0.7857             |
| DHT Humidity    | 372       | 34.17  | 48.6    | 28.0    | 2.4021             |


### Comparative analysis for the Humidity, Temperature, and atmospheric pressure levels for each Local and Remote location including mean, standard deviation, minimum, maximum, and median
```.py
# Example sensor data for temperature, humidity, and pressure collected from two sensors (BME280 and DHT11)
BME_Temp = [22.72, 22.75, 22.76, ...]       # Temperature readings (°C) from the BME280 sensor
BME_Hum = [32.29, 32.35, 32.32, ...]        # Humidity readings (%) from the BME280 sensor
BME_Pressure = [881.33, 881.42, 881.41, ...] # Pressure readings (hPa) from the BME280 sensor
DHT_Temp = [21.9, 22.1, 22.3, ...]          # Temperature readings (°C) from the DHT11 sensor
DHT_Hum = [31.5, 32.9, 32.2, ...]           # Humidity readings (%) from the DHT11 sensor

# Function to analyze a given list of sensor data
def analyze_sensor_data(sensor_data):
    """
    Analyzes a list of sensor data and returns key statistics: mean, standard deviation, minimum, and maximum.

    Parameters:
    sensor_data (list): List of numerical sensor readings.

    Returns:
    dict: A dictionary containing the mean, standard deviation, minimum, and maximum of the sensor data.
          If the input list is empty, returns None for all statistics.
    """

    # Check if the input data list is empty
    if not sensor_data:
        # If the list is empty, return a dictionary with None for all statistics
        return {"mean": None, "std_dev": None, "min": None, "max": None}

    # Calculate the mean (average) of the sensor data
    total = sum(sensor_data)               # Sum of all data points
    count = len(sensor_data)              # Number of data points
    mean = round(total / count)           # Compute mean and round to the nearest integer

    # Calculate the standard deviation (measure of data spread)
    # Variance is the average of the squared differences from the mean
    variance = (
        sum((x - mean) ** 2 for x in sensor_data) / (count - 1)
        if count > 1                        # Avoid division by zero for a single data point
        else 0                              # Variance is 0 when there's only one data point
    )
    std_dev = variance ** 0.5               # Standard deviation is the square root of the variance

    # Find the minimum and maximum values in the data
    min_value = min(sensor_data)            # Minimum value in the data
    max_value = max(sensor_data)            # Maximum value in the data

    # Return the calculated statistics in a dictionary
    return {
        "mean": mean,                       # Mean of the data
        "std_dev": std_dev,                 # Standard deviation of the data
        "min": min_value,                   # Minimum value
        "max": max_value                    # Maximum value
    }
```
### Code for prediction: Success Criteria 6
```.py
# Import necessary libraries
import pandas as pd  # For data manipulation and handling time-series data
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting and visualization
from numpy.polynomial.polynomial import Polynomial  # For fitting polynomial trends
import matplotlib  # For additional visualization settings

# Step 1: Define the dataset
# Historical sensor readings for temperature, humidity, and pressure from two sensors (BME and DHT).
# Example lists (replace `...` with actual data):
BME_Temp = [22.72, 22.75, ...]  # Temperature readings from the BME sensor
BME_Hum = [32.29, 32.35, ...]  # Humidity readings from the BME sensor
BME_Pressure = [881.33, 881.42, ...]  # Pressure readings from the BME sensor
DHT_Temp = [21.9, 22.1, 22.3, ...]  # Temperature readings from the DHT sensor
DHT_Hum = [31.5, 32.9, ...]  # Humidity readings from the DHT sensor

# Step 2: Create a DataFrame for time-series analysis
# Organizing the BME sensor data into a pandas DataFrame with a time index.
data = pd.DataFrame({
    'BME_Temp': BME_Temp,
    'BME_Hum': BME_Hum,
    'BME_Pressure': BME_Pressure
}, index=pd.date_range(start='2024-12-01', periods=len(BME_Temp), freq='h'))  # Time index in hourly intervals

# Step 3: Define an Auto-Regressive (AR) Model
# The AR model predicts the next 12 hours of readings for each column based on the mean of the last `lags` values.
def ar_model(data, lags=1):
    """
    Predict the next 12 time steps using a simple Auto-Regressive (AR) model.
    Parameters:
        - data: A DataFrame containing time-series data.
        - lags: Number of past time steps to use for forecasting.
    Returns:
        - forecast: A dictionary with predictions for each column in the data.
    """
    forecast = {}  # Dictionary to store forecasts for each column
    for col in data.columns:
        forecast[col] = []  # Initialize an empty list for the current column's forecast
        last_values = data[col].iloc[-lags:].values  # Get the last `lags` values as input for forecasting
        
        # Generate 12 forecasted values
        for _ in range(12):
            next_value = np.mean(last_values)  # Simple prediction: average of the last `lags` values
            forecast[col].append(next_value)  # Append the forecasted value
            last_values = np.append(last_values[1:], next_value)  # Update input values for the next prediction
    return forecast

# Step 4: Generate forecasts using the AR model
lags = 1  # Use the last 1 time step for predictions
forecast = ar_model(data[['BME_Temp', 'BME_Hum', 'BME_Pressure']], lags)

# Step 5: Create a future time index for the forecasts
# Time index for the next 12 hours based on the last timestamp in the data
future_index = pd.date_range(start=data.index[-1] + pd.Timedelta(hours=1), periods=12, freq='h')

# Step 6: Define a function to plot predictions and trends
def plot_with_trend(x_actual, y_actual, x_forecast, y_forecast, title, xlabel='Time', ylabel='Value', degree=2):
    """
    Plot actual and predicted data with polynomial trendlines.
    Parameters:
        - x_actual: Time index for the actual data.
        - y_actual: Actual data values.
        - x_forecast: Time index for the forecasted data.
        - y_forecast: Forecasted data values.
        - title: Title of the plot.
        - xlabel: Label for the x-axis.
        - ylabel: Label for the y-axis.
        - degree: Degree of the polynomial for trend fitting.
    """
    plt.figure(figsize=(10, 6))  # Set figure size
    
    # Plot actual data
    plt.plot(x_actual, y_actual, label='Actual', alpha=0.7)
    
    # Plot forecasted data
    plt.plot(x_forecast, y_forecast, label='Predicted', linestyle='dashed')
    
    # Fit and plot polynomial trend for actual data
    x_numeric_actual = np.arange(len(x_actual))  # Convert time index to numeric values
    poly_actual = Polynomial.fit(x_numeric_actual, y_actual, degree)  # Fit polynomial
    plt.plot(x_actual, poly_actual(x_numeric_actual), label='Actual Trend', linestyle='dotted', color='red')
    
    # Fit and plot polynomial trend for forecasted data
    x_numeric_forecast = np.arange(len(x_forecast)) + len(x_numeric_actual)  # Numeric indices for forecast
    poly_forecast = Polynomial.fit(x_numeric_forecast, y_forecast, degree)  # Fit polynomial
    plt.plot(x_forecast, poly_forecast(x_numeric_forecast), label='Forecast Trend', linestyle='dotted', color='green')
    
    # Add title, labels, and legend
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

# Step 7: Visualize the predictions with trends
# Generate plots for each column in the forecast
for col in forecast:
    plot_with_trend(
        x_actual=data.index,  # Time index of the actual data
        y_actual=data[col],  # Actual data values
        x_forecast=future_index,  # Time index of the forecasted data
        y_forecast=forecast[col],  # Forecasted data values
        title=f'{col} Prediction with Trend',  # Plot title
        degree=2  # Polynomial degree for trend fitting
    )
```
<img width="992" alt="Screenshot 2024-12-09 at 7 24 36" src="https://github.com/user-attachments/assets/268c1d09-b3f5-43a5-81d2-fcfd16c419cb">
<img width="998" alt="Screenshot 2024-12-09 at 7 25 03" src="https://github.com/user-attachments/assets/5aeba116-6a3d-41d1-89ab-596a454f9b9b">
<img width="998" alt="Screenshot 2024-12-09 at 7 25 25" src="https://github.com/user-attachments/assets/c8224720-cb1c-4422-bb46-437e047c275f">



## Criteria D: Functionality
A 7 min video demonstrating the proposed solution with narration

### References
1. Industries, A. (n.d.). DHT11 basic temperature-humidity sensor + extras https://www.adafruit.com/product/386
2. Indu, A., & Kumar, S. M. (2022). An Approach for Implementing Innovative Weather Monitoring System with DHT11 Sensor and Arduino Uno Tool based on IoT. In 2022 Sixth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC) (pp. 274-278).
3. Gurmu, M. D., & Qian, X. (2020). Automatic Room Temperature Control System Using Arduino UNO R3 and DHT11 Sensor. 2020 17th International Computer Conference on Wavelet Active Media Technology and Information Processing (ICCWAMTIP).
4. Hosny, K. M., Magdi, A., Salah, A., El-Komy, O., & Lashin, N. A. (2023). Internet of things applications using Raspberry-Pi: a survey. International Journal of Electrical and Computer Engineering (IJECE).
5. Virtanen, P., Gommers, R., Oliphant, T., Haberland, M., Reddy, T., Cournapeau, D., ... & Vázquez-Baeza, Y. (2019). SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature Methods, 17, 261-272.
6. What is Python?  Executive Summary. (n.d.). Python.org. https://www.python.org/doc/essays/blurb/
7. Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. ↩ ↩2
8. Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability QueryIs Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. ↩
9. Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. ↩
10. Espresso Outlet. (2024, September 27). Effects of Storage Conditions on Green Coffee Bean Quality: Investigating the Impact of Temperature, Humidity, and Storage Duration on Physical and Chemical Stability. Espresso Outlet LLC. https://espressooutlet.com/blogs/news/effects-of-storage-conditions-on-green-coffee-bean-quality-investigating-the-impact-of-temperature-humidity-and-storage-duration-on-physical-and-chemical-stability#:~:text=Degradation%20of%20Volatile%20Compounds%3A%20High,a%20less%20aromatic%20and%20less
