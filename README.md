# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

### Problem Definition
Our client, Mr. X, a boarding student at a local international school, is an avid coffee collector who values the rich aroma and flavor of premium coffee beans. However, he has grown increasingly concerned about the potential impact of humidity on the quality of his carefully curated collection. Fluctuating humidity levels in his pantry may lead to issues such as moisture absorption, mold growth, or a loss of freshness, all of which can compromise the beans' quality. Mr. X has already encountered some problems with declining bean quality. Ensuring the optimal storage conditions for his coffee has become a priority for Mr. X as he strives to preserve the distinct characteristics of his beans.

### Proposed Solution
To address the client’s requirements, a cost-effective and scalable solution includes a low-cost sensing device for humidity and temperature, combined with a custom data processing script for analyzing the acquired samples. For the sensing device, an excellent choice is the DHT11[1][2][3]sensor, which is available for less than $5 and provides adequate precision and range for the application (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). While alternatives like the DHT22, AHT20, or AM2301B offer higher specifications, the DHT11’s simplicity, using SPI communication instead of more complex protocols like I2C, makes it a better fit for this application.
To interface the DHT11 sensor with a computational platform, we proposed using a Raspberry Pi instead of an Arduino. The Raspberry Pi, starting at around $10 for the Raspberry Pi Zero, is a versatile, low-cost computer[4] that includes GPIO pins for direct sensor interfacing and runs a full operating system. Unlike the Arduino, which requires an additional computer to run the data processing software, the Raspberry Pi can both collect data and run the required Python scripts, consolidating the hardware into a single device. Its flexibility and computing power also make it easier to integrate additional functionalities, such as remote monitoring or cloud storage, should the client’s needs evolve.
Considering the budgetary constraints and system requirements, the proposed software tool for this solution is Python. Python's open-source nature, platform independence, and extensive library support[5][6] make it ideal for data analysis and visualization tasks. The language’s high abstraction level simplifies development and maintenance compared to lower-level alternatives like C or C++. Python’s automatic memory management and vast ecosystem of libraries ensure efficient development and seamless scalability for future enhancements. By leveraging Python on a Raspberry Pi, the system achieves a balance of simplicity, cost-effectiveness, and flexibility to meet the client’s needs.


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
Fig.3 Fig. 3 System diagram (HL+) for the proposed system to visualise and analyse temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides an API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.


### Task Planning
| **Task No.** | **Planned Action**                                                                                                              | **Planned Outcome**                                                                                                                  | **Time Estimate** | **Target Completion** | **Criteria** |
|--------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------|--------------|
| 1            | Take information from Dr. Ruben's GitHub                                                                                      | To have the proposed solution, success criteria, and system diagram                                                                 | 15 min            | Nov 16                | A, B         |
| 2            | Working on the problem definition and design statement                                                                            | To have a general view on the sensors needed, expected data, and the purpose of both local and remote measurements                  | 30 min            | Nov 17                | A            |
| 3            | Creating shared repository on GitHub                                                                                            | To have a centralized location for the project, including system diagrams, code, and data                                           | 10 min            | Nov 17                | B            |
| 4            | Setting up Raspberry Pi for sensor data collection (3 sensors for local measurements)                                             | To ensure the Raspberry Pi is able to collect Humidity, Temperature, and Atmospheric Pressure data locally in the dormitory         | 1 hour            | Nov 19                | C            |
| 5            | Working on functions for the code (Sensor data collection)                                                                       | To have modular functions that handle sensor data collection for each sensor individually, allowing clear code structure            | 3 hours           | Nov 21                | C            |
| 6            | Programming Raspberry Pi to collect data from 3 sensors                                                                           | To ensure that the Raspberry Pi can handle data collection from all 3 sensors, ensuring accurate local measurements                 | 1 hour            | Nov 23                | C            |
| 7            | Setting up the connection between local sensors                                                                                   | To test and verify connections between sensors on the Raspberry Pi to ensure proper data flow                                       | 45 min            | Nov 25                | C            |
| 8            | Testing sensor setup and reading local data                                                                                      | To ensure the sensors are correctly placed around the dormitory and data collection is accurate (Humidity, Temperature, and Atmospheric Pressure) | 30 min            | Nov 25                | C, B         |
| 9            | Storing local data in CSV format                                                                                                 | To ensure local data is saved in CSV files for later analysis                                                                        | 1 hour            | Nov 27                | C, SL        |
| 10           | Setting up cron jobs to run data collection every 5 minutes                                                                     | To automate the data collection process and ensure continuous data logging for 48+ hours                                            | 1 hour            | Nov 27                | C            |
| 11           | Uploading local data to remote server                                                                                           | To back up local data by sending it to a remote server for safekeeping and further analysis                                          | 30 min            | Nov 29                | C, HL        |
| 12           | Working on mathematical modeling for Humidity, Temperature, and Atmospheric Pressure                                           | To model the data collected, focusing on a non-linear model for local and remote locations                                          | 3 hours           | Nov 30                | HL           |
| 13           | Running comparative analysis of local and remote data                                                                           | To analyze the data, comparing mean, standard deviation, minimum, maximum, and median for Humidity, Temperature, and Atmospheric Pressure | 2 hours           | Dec 1                 | HL           |
| 14           | Prediction for the next 12 hours                                                                                                | To develop a predictive model for future Humidity, Temperature, and Atmospheric Pressure based on past data                         | 2 hours           | Dec 2                 | HL           |
| 15           | Creating visual representation of the data (graphs for local and remote locations)                                              | To visually represent the collected data for Humidity, Temperature, and Atmospheric Pressure                                        | 3 hours           | Dec 2                 | C, HL        |
| 16           | Analyzing and upgrading the graphs for better clarity                                                                           | To improve the visualizations, ensuring they are easy to interpret and contain necessary labels and trends                         | 2 hours           | Dec 4                 | C            |
| 17           | Creating flow diagrams for the code structure                                                                                   | To have a clear representation of the logic and flow of the code for future improvements and understanding                          | 1 hour            | Dec 5                 | B            |
| 18           | Designing the project poster                                                                                                   | To summarize the visual representations, mathematical models, and analysis. Include healthy level recommendations for Humidity, Temperature, and Atmospheric Pressure | 2 hours           | Dec 5                 | D            |
| 19           | Video outline creation for presentation                                                                                        | To determine the content and structure of the video presentation for the final results                                               | 20 min            | Dec 5                 | D            |
| 20           | Working on the final documentation                                                                                              | To document the entire project, including code, methods, data analysis, and conclusions                                             | 1 hour            | Dec 6                 | A, B, C      |
| 21           | Completing the poster with final results and recommendations                                                                   | To finalize the poster for presentation, ensuring clarity in visual data, models, and suggestions for healthy levels                | 4 hours           | Dec 7                 | D            |
| 22           | Recording and editing the project video                                                                                        | To produce a video summarizing the data collection, analysis, models, and the poster presentation                                  | 2 hours           | Dec 7                 | D            |


---

## Criteria C: Development

### Techniques Used
- Moving average for noise filtering.
- Data visualization using Matplotlib.
- API connections for data transmission.
- Predictive modeling of HL variables.
