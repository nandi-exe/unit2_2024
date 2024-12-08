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
Fig.3 Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables were measured locally with a network of DHT11/BMP280 sensors on a Raspberry Pi. A remote server provides an API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

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

## Criteria C: Development

### List of techniques used
#### Core Techniques
**1. Moving average for filtering noisy signals from sensors(with for loops inside)
**
Used to smooth sensor data and enhance model accuracy.
**2. Data visualization
**
Visualizing trends and patterns in collected data for analysis.
**3. Connecting to server using API
**
Establishing communication between the client and server for data exchange.
**4. Data models
**
Implementing mathematical models for prediction and analysis.
**5. File reading and modification
**
Handling CSV files for storing and accessing sensor data.
**6. Registering and Login into API
**
Managing user authentication and token-based access.
**7. Transmission of data to API servers
**
Sending serialized sensor data to a remote server.
**8. Accessing API data and readings
**
Fetching stored data for local use and further analysis.
#### Programming Constructs
1. Functions
2. Lists and Dictionaries
3. For loop
4. While loop
5. Try-except statement
6. If-else conditional statement
#### Libraries
**1. os
**For interacting with the operating system, e.g., file paths.
**2. time
**For delays and timestamp-related operations.
**3. csv
**Reading from and writing to CSV files for structured data storage.
**4. requests
**Making HTTP requests for API interactions.
**5. Adafruit - DHT11
**Accessing temperature and humidity readings from the DHT11 sensor.
**6. bme280
**Reading temperature, humidity, and pressure from the BME280 sensor.
**7. smbus2
**Reading temperature, humidity, and pressure from the BME280 sensor.
**8. datetime
**Managing date and time information for data logging.
**9. matplotlib
**Creating graphs and visualizations for data analysis.
**10. numpy
**Performing numerical computations and data manipulation.

### Data Collection and Sorting: Success Criteria 1 & 3 (Remote part)
This first part of the code is responsible for collecting data from the server, organizing it by sensor type, and ensuring that we have enough consecutive readings from all sensors.
**Step 1: Send a Request to Get Data
**
```.py
server_ip = "192.168.4.137"  # Server IP
response = requests.get(f"http://{server_ip}/readings")
data = response.json()
readings = data["readings"][0]
```
**What is it doing?
**This block sends a GET request to the server using the specified server_ip to fetch data. The data is then converted from JSON format into a Python dictionary. data["readings"][0] accesses the first set of readings, assuming this is the structure of the returned data.

**Step 2: Organizing Data by Sensor ID
**
```.py
# Organize data by sensor ID
temperature_data = []
humidity_data = []
pressure_data = []
timestamps = []

for r in readings:
    timestamp = datetime.fromisoformat(r["datetime"])
    if r["sensor_id"] == 11:  # Temperature
        temperature_data.append((timestamp, r["value"]))
    elif r["sensor_id"] == 10:  # Humidity
        humidity_data.append((timestamp, r["value"]))
    elif r["sensor_id"] == 12:  # Pressure
        pressure_data.append((timestamp, r["value"]))
```
**What is it doing?
**This block organizes the raw data into separate lists for temperature, humidity, and pressure, based on the sensor_id provided in the data. For each reading, it extracts the timestamp and value, storing them in tuples.

**Step 3: Sorting the Data
**
**What is it doing?
**This block sorts the data for each sensor type by the timestamp to ensure the readings are in chronological order. Sorting is essential for time-series data as we need to process it in a sequence.
**Step 4: Ensuring Consecutive Readings for Each Sensor
**
```.py
min_required = 2880  # 48 hours * 60 minutes

def find_last_consecutive(data, required_count):
    """Find the last block of consecutive readings of a given size."""
    for i in range(len(data) - required_count, -1, -1):
        timestamps_block = [data[j][0] for j in range(i, i + required_count)]
        # Check if timestamps are consecutive (1-minute intervals)
        if all((timestamps_block[j + 1] - timestamps_block[j]).seconds == 60 for j in range(len(timestamps_block) - 1)):
            return data[i : i + required_count]
    return []
```
**What is it doing?
**The function find_last_consecutive checks for the last block of 2880 consecutive readings (48 hours worth of data) from each sensor. The readings must be exactly one minute apart, so it checks if the time difference between consecutive readings is 60 seconds. If it finds such a block, it returns it; otherwise, it returns an empty list.
**Step 5: Applying the Consecutive Check to Each Sensor
**
```.py
# Find 2880 consecutive readings for each sensor
temperature_consecutive = find_last_consecutive(temperature_data, min_required)
humidity_consecutive = find_last_consecutive(humidity_data, min_required)
pressure_consecutive = find_last_consecutive(pressure_data, min_required)
```
**What is it doing?
**This applies the find_last_consecutive function to each of the sensor data lists (temperature, humidity, pressure) to ensure that we have at least 2880 consecutive readings from each sensor.

Step 6: Handling Insufficient Data
```.py
# Ensure all three sensors have enough data
if not temperature_consecutive or not humidity_consecutive or not pressure_consecutive:
    print("Error: Not enough consecutive data for one or more sensors.")
```
**What is it doing?
**This checks if any of the sensors failed to meet the requirement of 2880 consecutive readings. If so, it prints an error message.
**Step 7: Extracting Data from the Consecutive Readings
**
```.py
# Extract timestamps and values
timestamps = [t[0] for t in temperature_consecutive]
temperatures = [t[1] for t in temperature_consecutive]
humidities = [h[1] for h in humidity_consecutive]
pressures = [p[1] for p in pressure_consecutive]
```
**What is it doing?
**After ensuring there’s enough consecutive data, this step extracts the timestamps and sensor values (temperature, humidity, pressure) into separate lists.

##### Second Part: Finding Mathematical Models and Plotting the Data
This part fits mathematical models (sine and polynomial) to the sensor data and plots the results.

**Step 1: Convert Time to Minutes
**
```.py
# Extract time in minutes since the start
start_time = timestamps[0]
time_minutes = [(t - start_time).total_seconds() / 60 for t in timestamps]
```
**What is it doing?
**This converts the timestamps into "minutes since the start" (i.e., the time difference in minutes between each timestamp and the first timestamp). This is useful for fitting the models and working with time in a simpler numeric format.
**Step 2: Define the Mathematical Models
**
```.py
def sine_model(x, A, B, C, D):
    """Sine function for periodic data."""
    return A * np.sin(B * x + C) + D

def poly_model(x, a, b, c):
    """Quadratic polynomial for pressure."""
    return a * x**2 + b * x + c
```
**What is it doing?
**Here, two mathematical models are defined:
Sine model (sine_model): A sine wave model used for temperature and humidity, which has parameters A (amplitude), B (frequency), C (phase shift), and D (vertical shift).
Polynomial model (poly_model): A quadratic polynomial used for pressure, with parameters a, b, and c.
**Step 3: Fit the Models to the Data
**
```.py
# Fit models with adjusted initial guesses
temp_params, temp_cov = curve_fit(sine_model, time_minutes, temperatures, p0=[3, 0.003, 0, 26])
humidity_params, humidity_cov = curve_fit(sine_model, time_minutes, humidities, p0=[2, 0.003, 0, 16])
pressure_params, pressure_cov = curve_fit(poly_model, time_minutes, pressures)
```
**What is it doing?
**The curve_fit function from SciPy is used to fit the models (sine_model for temperature and humidity, poly_model for pressure) to the data.
The initial guesses p0 for the sine model are provided for temperature and humidity.
For pressure, a polynomial model is fitted.
**Step 4: Generate Predictions from the Models
**
```.py
# Generate predictions
time_fit = np.linspace(0, max(time_minutes), 1000)  # More points for a smoother curve
temp_fit = sine_model(time_fit, *temp_params)
humidity_fit = sine_model(time_fit, *humidity_params)
pressure_fit = poly_model(time_fit, *pressure_params)
```
**What is it doing?
**Here, the time_fit is created as a more granular time array (1000 points) over the range of the original time data. Predictions for temperature, humidity, and pressure are then generated using the fitted models (temp_fit, humidity_fit, pressure_fit).
**Step 5: Plotting the Data and Models
**
```.py
# Plot original data and fits
plt.figure(figsize=(12, 10))

# Temperature
plt.subplot(3, 1, 1)
plt.plot(time_minutes, temperatures, color="red", label="Data")
plt.plot(time_fit, temp_fit, color="blue", label="Sine Model Fit")
plt.title("Temperature Model")
plt.legend()
plt.grid()

# Humidity
plt.subplot(3, 1, 2)
plt.plot(time_minutes, humidities, color="blue", label="Data")
plt.plot(time_fit, humidity_fit, color="green", label="Sine Model Fit")
plt.title("Humidity Model")
plt.legend()
plt.grid()

# Pressure
plt.subplot(3, 1, 3)
plt.plot(time_minutes, pressures, color="green", label="Data")
plt.plot(time_fit, pressure_fit, color="purple", label="Polynomial Model Fit")
plt.title("Pressure Model")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
```
**What is it doing?
****This step creates the plots:
**The first subplot shows the original temperature data and the fitted sine model.
The second subplot shows the original humidity data and the fitted sine model.
The third subplot shows the original pressure data and the fitted polynomial model. Each subplot contains the original data and the model fits with legends and gridlines.

This part fits sine and polynomial models to the sensor data and generates the corresponding plots. It provides a mathematical representation of the temperature, humidity, and pressure data.




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
