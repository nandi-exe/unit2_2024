# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

### Problem Definition
The client, Mr. X, is a boarding student at a local international school and a passionate coffee enthusiast. As a dedicated collector of premium coffee beans, he takes great pride in preserving their rich aroma, complex flavors, and overall quality. His deep appreciation for coffee's nuanced characteristics drives his attention to detail in maintaining the integrity of his collection. However, Mr. X has faced persistent challenges with fluctuating humidity levels in his pantry, which have led to moisture absorption, mold growth, and a noticeable decline in freshness. These issues have significantly compromised the quality of his carefully curated beans, undermining his ability to fully enjoy their distinct profiles. Determined to protect his collection, Mr. X has made it a top priority to establish optimal storage conditions. Recognizing the detrimental impact of inconsistent humidity on his coffee beans, he is actively seeking a reliable and effective solution to safeguard their unique qualities. By addressing these environmental factors, Mr. X hopes to preserve the full essence of his beans and elevate his coffee-collecting experience.
(_See the evidence of Consultation in the Appendix: Criteria B/Record of Tasks_)

### Proposed Solution

To address the client’s requirements, a cost-effective and scalable solution includes a low-cost sensing device for humidity and temperature, combined with a custom data processing script for analyzing the acquired samples. For the sensing device, an excellent choice is the DHT11 [[1]](https://www.adafruit.com/product/386) [[2]](https://www.researchgate.net/publication/366522967_An_Approach_for_Implementing_Innovative_Weather_Monitoring_System_with_DHT11_Sensor_and_Arduino_Uno_Tool_based_on_IoT) [[3]](https://www.researchgate.net/publication/350859817_Automatic_Room_Temperature_Control_System_Using_Arduino_UNO_R3_and_DHT11_Sensor) sensor, which is available for less than $5 and provides adequate precision and range for the application (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). While alternatives like the DHT22, AHT20, or AM2301B offer higher specifications, the DHT11’s simplicity, using SPI communication instead of more complex protocols like I2C, makes it a better fit for this application.

To interface the DHT11 sensor with a computational platform, we proposed using a Raspberry Pi instead of an Arduino. The Raspberry Pi, starting at around $10 for the Raspberry Pi Zero, is a versatile, low-cost computer [[4]](https://ijece.iaescore.com/index.php/IJECE/article/view/27879) that includes GPIO pins for direct sensor interfacing and runs a full operating system. Unlike the Arduino, which requires an additional computer to run the data processing software, the Raspberry Pi can both collect data and run the required Python scripts, consolidating the hardware into a single device. Its flexibility and computing power also make it easier to integrate additional functionalities, such as remote monitoring or cloud storage, should the client’s needs evolve.

Considering the budgetary constraints and system requirements, the proposed software tool for this solution is Python. Python's open-source nature, platform independence, and extensive library support [[5]](https://www.nature.com/articles/s41592-019-0686-2) [[6]](https://www.python.org/doc/essays/blurb/) make it ideal for data analysis and visualization tasks. The language’s high abstraction level simplifies development and maintenance compared to lower-level alternatives like C or C++ [[7]](https://realpython.com/python-vs-cpp/#memory-management). Python’s automatic memory management and vast ecosystem of libraries ensure efficient development and seamless scalability for future enhancements [[8]](https://github.com/tino/pyFirmata) [[9]](https://pythongeeks.org/advantages-disadvantages-of-python/). By leveraging Python on a Raspberry Pi, the system achieves a balance of simplicity, cost-effectiveness, and flexibility to meet the client’s needs.

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


### References for Criteria A
1. Industries, A. (n.d.). DHT11 basic temperature-humidity sensor + extras https://www.adafruit.com/product/386
2. Indu, A., & Kumar, S. M. (2022). An Approach for Implementing Innovative Weather Monitoring System with DHT11 Sensor and Arduino Uno Tool based on IoT. In 2022 Sixth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC) (pp. 274-278).
3. Gurmu, M. D., & Qian, X. (2020). Automatic Room Temperature Control System Using Arduino UNO R3 and DHT11 Sensor. 2020 17th International Computer Conference on Wavelet Active Media Technology and Information Processing (ICCWAMTIP).
4. Hosny, K. M., Magdi, A., Salah, A., El-Komy, O., & Lashin, N. A. (2023). Internet of things applications using Raspberry-Pi: a survey. International Journal of Electrical and Computer Engineering (IJECE).
5. Virtanen, P., Gommers, R., Oliphant, T., Haberland, M., Reddy, T., Cournapeau, D., ... & Vázquez-Baeza, Y. (2019). SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature Methods, 17, 261-272.
6. What is Python?  Executive Summary. (n.d.). Python.org. https://www.python.org/doc/essays/blurb/
7. Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. ↩ ↩2
8. Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability QueryIs Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. ↩
9. Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. ↩

---

## Criteria B: Design
### System Diagrams

![systemdiagram](https://github.com/user-attachments/assets/dba28917-4f10-44b0-898e-e894d8960afa)
Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables were measured locally with a network of DHT11/BMP280 sensors on a Raspberry Pi. A remote server provides an API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

### Flow Diagram 1
![image](https://github.com/user-attachments/assets/3c5fbc87-14d6-4479-8573-7bd1673e8dc8)
Fig 1.1.1: A flowchart showing how our sensor registration code is implemented. It ensures that each sensor is registered to the API, giving us a place to send our sensor data once it has been collected.
### Flow Diagram 2
![image](https://github.com/user-attachments/assets/af8eda74-9a3a-46e0-b612-4b913ffbdccb)
Fig 1.1.2: A flowchart showcasing how our data is saved to the local csv file (sensor_data.csv).

### Flow Diagram 3
![image](https://github.com/user-attachments/assets/c4efa4a5-b884-4ad1-8bcd-20a8bd77204f)
Fig 1.1.3: A flowchart showcasing how the relevant data is filtered from the API.


Both Fig 1.1.2 and 1.1.3 include logging in at every iteration, because the login token would expire after 15 iterations, so we decided to add that step to every upload (explained more in Criteria C, commented code) just to play it safe.

### How is the data stored and managed?
The collected data is stored locally in a CSV file for structured access and offline analysis. This format allows for easy reading, modification, and integration with data-processing tools. To ensure data persistence and accessibility, the CSV data is periodically uploaded to an API server. This two-tiered approach balances local storage for quick access with remote storage for backup and broader analysis, providing a reliable and scalable system for managing the collected environmental data.

<img width="881" alt="image" src="https://github.com/user-attachments/assets/0312f0c4-62a1-4b52-9fd8-e863f8cf8e2d" />
Fig 1.2.1 The data as stored in the csv file, sensor_data.csv".

![image](https://github.com/user-attachments/assets/cc73334c-0f75-49a0-a3fc-f52a470ac78b)
Fig 1.2.2 The table formed using the data for the client's readability.

The remote collected data is stored in an API (explained more in the system diagram), allowing easy access.

![image](https://github.com/user-attachments/assets/a02f4aea-67ab-4e4c-af3b-b7aa13576b4a)
Fig 1.2.3 The data as is stored within the API. For it to become readable, one would need to extract it from the server using a request.



### Record of Tasks
# Record of Tasks

| Task No | Planned Action                                | Planned Outcome                                                    | Time Estimate | Target Completion Date | Criteria   |
|---------|----------------------------------------------|----------------------------------------------------------------------|---------------|-------------------------|------------|
| 1       | Consult with the client                      | Understand the client's needs and refine project goals               | 30 mins       | Nov 15                 | A          |
| 2       | Write problem definition, design statement, and success criteria | Finalize problem definition, design statement, and criteria for evaluation | 15 mins      | Nov 16                 | A, B       |
| 3       | Research sensors and purpose of local and remote measurements | Identify sensors needed and their purpose for data collection          | 30 mins      | Nov 17                 | A          |
| 4       | Create GitHub repository, fork template | Centralize project files, including system diagrams, code, and data     | 10 mins      | Nov 17                 | B          |
| 5       | Complete system diagram                      | Create a diagram representing the hardware and software components    | 20 mins      | Nov 18                 | B          |
| 6       | Develop detailed criteria                   | Define criteria the program will follow to ensure functionality       | 20 mins      | Nov 19                 | A          |
| 7       | Set up Raspberry Pi for sensor data collection | Collect temperature, humidity, and pressure data locally               | 1 hour       | Nov 19                 | C          |
| 8       | Develop modular functions for sensor data collection | Organize, refactor, and modularize code for handling data from each sensor                     | 3 hours      | Nov 21                 | C          |
| 9       | Program Raspberry Pi to integrate and collect data | Enable data collection from DHT11 and BME280 sensors                   | 1 hour       | Nov 23                 | C          |
| 10      | Test connections between sensors             | Ensure accurate data flow between sensors and Raspberry Pi            | 45 mins      | Nov 25                 | C          |
| 11      | Complete calendar interface                  | Develop a disguised calendar interface with interactive features      | 2.5 hours     | Nov 26                 | C          |
| 12      | Test sensor placement and data accuracy      | Verify sensor setup and accurate collection of temperature, humidity, pressure | 30 mins | Nov 25 | C, B |
| 13      | Save local data in CSV format                | Store data in a structured format for analysis                        | 1 hour       | Nov 27                 | C, SL      |
| 14      | Automate data collection                     | Schedule data collection every minute for continuous logging          | 1 hour       | Nov 27                 | C          |
| 15      | Automate uploading local data to remote server | Back up local data on a remote server                                | 30 mins      | Nov 29                 | C, HL      |
| 16      | Develop mathematical models for data         | Create models for temperature, humidity, and pressure data            | 3 hours      | Nov 30                 | HL         |
| 17      | Analyze local and remote data                | Compare key statistics (mean, median, range, etc.) for data           | 2 hours      | Dec 1                  | HL         |
| 18      | Predict future trends                        | Use past data to model 12-hour forecasts for environmental parameters | 2 hours      | Dec 2                  | HL         |
| 19      | Create graphs to visualize data              | Plot data trends for temperature, humidity, and pressure              | 3 hours      | Dec 2                  | C, HL      |
| 20      | Refine data visualizations                   | Improve clarity and design of graphs with labels and trends           | 2 hours      | Dec 4                  | C          |
| 21      | Complete flow diagrams                       | Create diagrams representing code structure and logic                 | 1 hour       | Dec 5                  | B          |
| 22      | Record a demonstration                       | Provide the client a preview of the product for feedback              | 20 mins      | Dec 6                  | D          |
| 23      | Draft scientific poster                      | Summarize data, models, and recommendations on a poster               | 2 hours      | Dec 5                  | D          |
| 24      | Plan video presentation outline              | Structure the content for the project video                           | 20 mins      | Dec 5                  | D          |
| 25      | Complete final documentation                 | Compile project documentation, including code and analysis            | 1 hour       | Dec 6                  | A, B, C    |
| 26      | Finalize scientific poster                   | Include refined graphs and conclusions summarizing the investigation  | 4 hours      | Dec 7                  | D          |
| 27      | Record and edit project video                | Create a video summarizing the solution, analysis, and poster         | 2 hours      | Dec 7                  | D          |
| 28      | Submit project to client for feedback        | Send our Github repository to the client to showcase our process, and get feedback on the solution and advice.| 5 mins      | Dec 9                  | A,B,C,D |
| 29      | Improve on client feedback to make the project more helpful | Work on the feedback that the client has given us in order to improve our project and help the client better. | 3 hours      | Dec 12                  | A,B,C,D |


### Test Plan

#### more potential

| Test Type            | Target                                                                 | Procedure                                                                                                                   | Expected Outcome                                                                                              |
|----------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Test 1**            | **Visual Representation of HL values (Local & Remote) for 48 hours**   | 1. Connect sensors to the Raspberry Pi:                                                                                     | Visual representation of Humidity, Temperature, and Atmospheric Pressure (HL) values for both Local and Remote locations for at least 48 hours. |
|                      |                                                                        |   - BME280: VIN - 3.3V or 5V, GND - GND, SCL - GPIO 3, SDA - GPIO 2                                                          |                                                                                                               |
|                      |                                                                        |   - DHT11: VCC - 3.3V, GND - GND, DATA - GPIO 17                                                                           |                                                                                                               |
|                      |                                                                        | 2. Run `main.py` to collect data from sensors.                                                                              |                                                                                                               |
|                      |                                                                        | 3. Run `extract_data.py` to generate time-series graphs for Humidity, Temperature, and Pressure (HL) values.              |                                                                                                               |
|                      |                                                                        | 4. Verify that the graphs display time-series data for both Local and Remote locations over 48 hours.                      |                                                                                                               |
| **Test 2**            | **Measure Local Variables with 3 Sensors**                            | 1. Place three sensors (e.g., BME280 and DHT11) in different parts of the dormitory.                                        | CSV file should show data from three sensors, confirming simultaneous data collection for the entire dormitory.|
|                      |                                                                        | 2. Run `main.py` to collect data for all three sensors simultaneously.                                                     |                                                                                                               |
|                      |                                                                        | 3. Open the generated CSV file and verify that data from all sensors is recorded.                                           |                                                                                                               |
| **Test 3**            | **Mathematical Modelling for HL levels (Linear & Non-Linear)**         | 1. Ensure 48 hours of data has been collected and stored in the CSV file.                                                    | Both linear and non-linear models should be generated for each variable, including equations and graphs.       |
|                      |                                                                        | 2. Run `modelling.py` to create linear and non-linear models for Humidity, Temperature, and Atmospheric Pressure (HL).     |                                                                                                               |
|                      |                                                                        | 3. Verify that model equations and graphs are produced for both Local and Remote data.                                      |                                                                                                               |
| **Test 4**            | **Comparative Analysis for HL levels**                                | 1. Collect at least 48 hours of data from sensors.                                                                           | Statistical analysis should produce accurate mean, standard deviation, minimum, maximum, and median values for all variables and locations.|
|                      |                                                                        | 2. Run `statistics.py` to calculate and output the statistical values (mean, standard deviation, etc.) for both locations. |                                                                                                               |
|                      |                                                                        | 3. Cross-check the results with a spreadsheet application for accuracy.                                                    |                                                                                                               |
| **Test 5**            | **Data Storage and Backup to Remote Server**                          | 1. Run `main.py` to collect and store data in a CSV file.                                                                   | Data should be stored locally in the CSV file and uploaded to the remote server successfully.                  |
|                      |                                                                        | 2. Verify that the data is saved in the CSV file by opening File Explorer on the Raspberry Pi.                             |                                                                                                               |
|                      |                                                                        | 3. Run `checkifuploaded.py` to confirm that the data has been successfully uploaded to the server.                         |                                                                                                               |
| **Test 6**            | **Prediction for the Subsequent 12 Hours for HL variables**           | 1. Collect 48 hours of data for training the predictive model.                                                              | Predictions for the next 12 hours should be generated and visualized for each variable, with accuracy checked.  |
|                      |                                                                        | 2. Run `predict.py` to generate predictions for Humidity, Temperature, and Atmospheric Pressure (HL).                      |                                                                                                               |
|                      |                                                                        | 3. Verify that predicted values are generated and plotted on graphs.                                                        |                                                                                                               |
|                      |                                                                        | 4. Compare the predicted data with actual measurements after the 12-hour period for accuracy.                              |                                                                                                               |
| **Test 7**            | **Poster Summary with Recommendations for HL levels**                | 1. Gather all generated graphs, models, and statistical analysis results.                                                   | A well-designed poster summarizing the project, including graphs, models, statistical analysis, and actionable recommendations for storage conditions should be created. |
|                      |                                                                        | 2. Use a design tool like Canva or PowerPoint to create the poster.                                                         |                                                                                                               |
|                      |                                                                        | 3. Include a clear summary of findings and actionable recommendations for optimal storage conditions.                      |                                                                                                               |
|                      |                                                                        | 4. Review the poster for accuracy, clarity, and completeness.                                                              |                                                                                                               |


### Potential test plan instead of other one

| **Success Criteria** | **Description** | **Test Procedure** | **Expected Outcome** |
|----------------------|-----------------|--------------------|---------------------|
| **1** | Visual representation of Humidity, Temperature, and Atmospheric Pressure (HL) values for at least 48 hours (Local and Remote). | 1. Connect the BME280 and DHT11 sensors to the Raspberry Pi.<br>2. Power on the Raspberry Pi.<br>3. Run the `main.py` script to collect data for at least 48 hours.<br>4. Use `extract_data.py` to generate time-series graphs.<br>5. Verify graphs display data for Local and Remote locations. | Time-series graphs should show data for Humidity, Temperature, and Pressure (Local and Remote) over at least 48 hours. |
| **2** | Measure Humidity, Temperature, and Atmospheric Pressure (HL) using 3 sensors in the dormitory. | 1. Place three BME280 sensors in different parts of the dormitory.<br>2. Connect all sensors to the Raspberry Pi.<br>3. Run the `main.py` script to collect data simultaneously.<br>4. Verify the CSV file contains data from all three sensors. | The CSV file should confirm measurements are collected simultaneously from all three sensors. |
| **3** | Create mathematical models for Humidity, Temperature, and Atmospheric Pressure (HL) for Local and Remote locations. | 1. Collect at least 48 hours of data.<br>2. Run `modelling.py` to generate linear and non-linear models.<br>3. Verify that equations and graphs are generated for each variable. | Linear and non-linear models, including equations and graphs, should be generated for each variable (Local and Remote). |
| **4** | Perform a comparative analysis for Humidity, Temperature, and Atmospheric Pressure (HL). | 1. Collect at least 48 hours of data.<br>2. Run `statistics.py` to calculate mean, standard deviation, minimum, maximum, and median.<br>3. Verify statistical values are computed correctly. | Statistical analysis should produce accurate mean, standard deviation, minimum, maximum, and median values. |
| **5** | Store Local data in a CSV file and upload it to a remote server. | 1. Collect data using the procedure in Success Criteria 1.<br>2. Verify data is saved locally in a CSV file.<br>3. Run `upload_to_server.py` to upload the CSV file to a remote server.<br>4. Use `checkifuploaded.py` to confirm the upload. | Data should be stored locally and successfully uploaded to the remote server for backup. |
| **6** | Provide a 12-hour prediction for Humidity, Temperature, and Atmospheric Pressure (HL). | 1. Collect at least 48 hours of data.<br>2. Run `predict.py` to generate 12-hour predictions.<br>3. Verify predicted values and visualizations.<br>4. Compare predictions with actual subsequent measurements. | 12-hour predictions for each variable should be generated, visualized, and show trends and anticipated values. |
| **7** | Create a poster summarizing visual representations, models, analysis, and recommendations. | 1. Compile outputs from previous procedures.<br>2. Use a design tool to create the poster.<br>3. Include visual representations, analysis, models, and recommendations.<br>4. Review for clarity, accuracy, and visual appeal. | A well-designed poster summarizing the project, including graphs, models, analysis, and actionable recommendations, should be created. |


# Test Plan


| **Test Type**           | **Target**                                                                                  | **Procedure**                                                                                                                                                                                                                     | **Expected Outcome**                                                                                                                                                       |
|--------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect sensors & power  | Connect BME280 and DHT11 sensors to Raspberry Pi.                                          | **BME280:**<br>VIN - 3.3V or 5V (2C1R)<br>GND - GND (2C3R)<br>SCL - GPIO 3 (1C2R)<br>SDA - GPIO 2 (1C3R)<br><br>**DHT11:**<br>VCC - 3.3V (1C1R)<br>GND - GND (1C4R)<br>DATA - GPIO (1C5R)<br> Connect the micro-USB cable to the charging brick and a power source. | Sensors should be securely connected to the Raspberry Pi, ready for data collection.                                                                                      |
| Find Raspberry Pi IP     | Locate the IP address of the Raspberry Pi.                                                 | **Method 1: Using Angry IP Scanner**<br>1. Install Angry IP Scanner on your computer.<br>2. Open the scanner and click "Start." <br>3. Locate the Raspberry Pi in the list of detected devices by its hostname.<br><br>**Method 2: Using a Display**<br>1. Connect the Raspberry Pi to a monitor and keyboard.<br>2. Hover over the Wi-Fi symbol in the taskbar.<br>3. Note the displayed IP address. | The Raspberry Pi’s IP address should be successfully identified for remote access.                                                                                          |
| Connect to Raspberry Pi  | Access Raspberry Pi desktop remotely using VNC Viewer.                                     | Install VNC Viewer on your computer. <br>Open VNC Viewer.<br>Type in the Raspberry Pi’s IP address.<br>Enter username: **MIKEANDUNANDI** and password: **ANYTHINGMEMORABLE123**.                                                                                          | The desktop of the Raspberry Pi should be displayed.                                                                                                                       |
| Run main.py              | Connect to the server and collect sensor data.                                             | Open the terminal and type the following commands line by line:<br>`python3 -m venv venv`<br>`source venv/bin/activate`<br>`python3 main.py`<br>Every minute, the terminal should display the data collected and verification messages. | A message displaying data from each sensor should pop up on the terminal every minute, along with verification statements.                                                 |
| Check CSV file           | Verify if data has been added to the CSV file after running the main code.                 | Open the File Explorer on the Raspberry Pi.<br>Navigate to the directory containing the CSV file.<br>Open the CSV file and confirm that new data entries have been added.                                                         | The CSV file should contain newly added data entries after running the main code.                                                                                         |
| Check API upload         | Verify if the data is uploaded to the API.                                                 | Open PyCharm.<br>Run `checkifuploaded.py`.                                                                                                                                                                                        | The program should confirm whether the collected data has been successfully uploaded to the API.                                                                           |
| Model the data           | Create graphs of collected and predicted data.                                             | Open PyCharm.<br>Run `extract_data.py`.                                                                                                                                                                                          | The program should produce 6 graphs:<br>- 2 for Temperature<br>- 2 for Humidity<br>- 2 for Pressure (collected and predicted).                                             |
| Produce statistics       | Calculate and display minimum, maximum, and average values for each sensor.                | Open PyCharm.<br>Run `statistics.py`.                                                                                                                                                                                            | The program should produce the minimum, maximum, and average values for each sensor.                                                                                      |

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

### Challenge 1: Login Timeout

During our first round of data collection we realised that after 15 minutes, the server would deny us access to the server, resulting in only the csv file being updated and not the server. After consulting other project developers, and reading (some kind of source about APIs) we realised the problem was in the access token. 

After compiling the modules into the main file, we had left the server login code outside of the “send to server” module. By doing so, the code only logged into the server once throughout the entire 48 hours. What we didn’t realise was that the access token gained from this initial login in  timed out after 15 iterations/minutes, which resulted in the data upload being halted once this time frame elapsed.

#### Solution

In order to combat this error, we shifted the following code into the “upload_to_server” module. With this change, each iteration of the upload had the Raspberry refresh the login credentials, preventing the time_out error we were receiving and allowing all the data to upload efficiently.

```
 try:
        login_response = requests.post(f'http://{server_ip}/login', json=user)
        cookie = login_response.json().get('access_token')
        if not cookie:
            raise ValueError("Failed to retrieve access token. Check login credentials.")

        auth = {'Authorization': f'Bearer {cookie}'}

```


### References for Criteria C: Helpful sources during our project development
[This video helped us understand how to connect the sensors to the Raspberry Pi correctly](https://youtu.be/T7L7WMHbhY0?si=WClVVa0leFPAXtXl)

## Criteria D: Functionality
A 7 min video demonstrating the proposed solution with narration - sent
POSTER
[CD.pdf](https://github.com/user-attachments/files/18054644/CD.pdf)

### References for Poster
10. Espresso Outlet. (2024, September 27). Effects of Storage Conditions on Green Coffee Bean Quality: Investigating the Impact of Temperature, Humidity, and Storage Duration on Physical and Chemical Stability. Espresso Outlet LLC. https://espressooutlet.com/blogs/news/effects-of-storage-conditions-on-green-coffee-bean-quality-investigating-the-impact-of-temperature-humidity-and-storage-duration-on-physical-and-chemical-stability#:~:text=Degradation%20of%20Volatile%20Compounds%3A%20High,a%20less%20aromatic%20and%20less
