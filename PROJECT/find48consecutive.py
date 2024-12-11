import requests
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from datetime import datetime

server_ip = "192.168.4.137"
response = requests.get(f"http://{server_ip}/readings")
data = response.json()
readings = data["readings"][0]

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

# Sort all data by timestamps
temperature_data.sort(key=lambda x: x[0])
humidity_data.sort(key=lambda x: x[0])
pressure_data.sort(key=lambda x: x[0])

# Ensure all sensors have at least 2880 consecutive readings
min_required = 2880  # 48 hours * 60 minutes

def find_last_consecutive(data, required_count):
    """Find the last block of consecutive readings of a given size."""
    for i in range(len(data) - required_count, -1, -1):
        timestamps_block = [data[j][0] for j in range(i, i + required_count)]
        # Check if timestamps are consecutive (1-minute intervals)
        if all((timestamps_block[j + 1] - timestamps_block[j]).seconds == 60 for j in range(len(timestamps_block) - 1)):
            return data[i : i + required_count]
    return []

# Find 2880 consecutive readings for each sensor
temperature_consecutive = find_last_consecutive(temperature_data, min_required)
humidity_consecutive = find_last_consecutive(humidity_data, min_required)
pressure_consecutive = find_last_consecutive(pressure_data, min_required)

# Ensure all three sensors have enough data
if not temperature_consecutive or not humidity_consecutive or not pressure_consecutive:
    print("Error: Not enough consecutive data for one or more sensors.")
else:
    # Extract timestamps and values
    timestamps = [t[0] for t in temperature_consecutive]
    temperatures = [t[1] for t in temperature_consecutive]
    humidities = [h[1] for h in humidity_consecutive]
    pressures = [p[1] for p in pressure_consecutive]

    # Plot the data in subplots
    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.plot(timestamps, temperatures, color="red", label="Temperature (°C)")
    plt.title("Temperature Over the Last 48 Hours")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(timestamps, humidities, color="blue", label="Humidity (%)")
    plt.title("Humidity Over the Last 48 Hours")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(timestamps, pressures, color="green", label="Pressure (hPa)")
    plt.title("Pressure Over the Last 48 Hours")
    plt.xlabel("Time")
    plt.ylabel("Pressure (hPa)")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


# Extract time in minutes since the start
start_time = timestamps[0]
time_minutes = [(t - start_time).total_seconds() / 60 for t in timestamps]

# Define potential models
def sine_model(x, A, B, C, D):
    """Sine function for periodic data."""
    return A * np.sin(B * x + C) + D

def poly_model(x, a, b, c):
    """Quadratic polynomial for pressure."""
    return a * x**2 + b * x + c

# Fit models with adjusted initial guesses
# Temperature (sine model)
temp_params, temp_cov = curve_fit(sine_model, time_minutes, temperatures, p0=[3, 0.003, 0, 26])
# Humidity (sine model)
humidity_params, humidity_cov = curve_fit(sine_model, time_minutes, humidities, p0=[2, 0.003, 0, 16])
# Pressure (polynomial model)
pressure_params, pressure_cov = curve_fit(poly_model, time_minutes, pressures)

# Generate predictions
time_fit = np.linspace(0, max(time_minutes), 1000)  # More points for a smoother curve
temp_fit = sine_model(time_fit, *temp_params)
humidity_fit = sine_model(time_fit, *humidity_params)
pressure_fit = poly_model(time_fit, *pressure_params)

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

# Print parameters
print("Temperature Model Parameters (Sine):", temp_params)
print("Humidity Model Parameters (Sine):", humidity_params)
print("Pressure Model Parameters (Polynomial):", pressure_params)
