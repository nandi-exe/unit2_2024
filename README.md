# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

### Problem Definition
Our client, **Mr. X**, a boarding student at a local international school, is an avid coffee collector concerned about the potential impact of humidity on his coffee beans. Fluctuating humidity levels in his pantry have led to issues like moisture absorption, mold growth, and loss of freshness. Ensuring optimal storage conditions has become a priority to preserve the distinct characteristics of his collection.

### Proposed Solution
A **cost-effective and scalable solution** includes:
- **Hardware**: A DHT11 sensor (< $5), chosen for simplicity and adequate precision (Temperature: 0–50°C, Humidity: 20–90%), paired with a Raspberry Pi Zero (starting at $10).
- **Software**: Python for data analysis and visualization, leveraging libraries for ease of use and scalability.

### Success Criteria
1. Visual representation of humidity, temperature, and atmospheric pressure (HL) inside and outside over 48+ hours.
2. Local variables measured with three sensors in the dormitory.
3. Mathematical modeling for HL variables using linear (SL) and non-linear (HL) models.
4. Comparative analysis of HL values (mean, std dev, min, max, median).
5. Data storage in CSV (SL) and remote server backup (HL).
6. Prediction of HL levels for the next 12 hours.
7. A poster summarizing findings and recommending optimal HL levels.

---

## Criteria B: Design

### System Diagrams
- **SL**: Local measurements with DHT11 on Arduino.
- **HL**: Network of DHT11/BMP280 sensors with Raspberry Pi and remote server.
- **HL+**: Enhanced system with remote work laptop and ISAK-S network API.

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
