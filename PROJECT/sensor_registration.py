import requests

# Define the server IP address where the API is hosted
server_ip = "192.168.4.137"

# User credentials for login
user = {'username': 'UNANDI', 'password': 'nananandi08'}

# Step 1: Login to the server to authenticate the user
# Send a POST request to the /login endpoint with the user credentials
answer = requests.post(f'http://{server_ip}/login', json=user)

# Print the raw JSON response for debugging purposes
print(answer.json())
print("happy")  # Indicating the login process was attempted

# Step 2: Extract the access token from the login response
login_response = requests.post(f'http://{server_ip}/login', json=user)
cookie = login_response.json().get('access_token')

# Validate if the token was successfully retrieved
if not cookie:
    raise ValueError("Failed to retrieve access token. Check login credentials.")

# Authorization header with the Bearer token for secure API requests
auth = {'Authorization': f'Bearer {cookie}'}

# Step 3: Register sensors in the system
# DHT11 Temperature sensor details
dht_t = {
    "type": "Temperature",  # Type of sensor
    "location": "Basil's Room",  # Physical location of the sensor
    "name": "unami_dht_t",  # Unique identifier for the sensor
    "unit": "C"  # Measurement unit
}
# Send a POST request to register the DHT11 temperature sensor
r = requests.post(f'http://{server_ip}/sensor/new', json=dht_t, headers=auth)
print(f'DHT Temperature: {r.json}')  # Print the response from the server

# DHT11 Humidity sensor details
dht_h = {
    "type": "Humidity",
    "location": "Basil's Room",
    "name": "unami_dht_h",
    "unit": "%"
}
# Send a POST request to register the DHT11 humidity sensor
r = requests.post(f'http://{server_ip}/sensor/new', json=dht_h, headers=auth)
print(f'DHT Humidity: {r.json}')  # Print the response from the server

# BMP280 Temperature sensor details
bmp_t = {
    "type": "Temperature",
    "location": "Basil's Room",
    "name": "unami_bmp_t",
    "unit": "C"
}
# Send a POST request to register the BMP280 temperature sensor
r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_t, headers=auth)
print(f'BMP Temperature: {r.json}')  # Print the response from the server

# BMP280 Humidity sensor details
bmp_h = {
    "type": "Humidity",
    "location": "Basil's Room",
    "name": "unami_bmp_h",
    "unit": "%"
}
# Send a POST request to register the BMP280 humidity sensor
r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_h, headers=auth)
print(f'BMP Humidity: {r.json}')  # Print the response from the server

# BMP280 Pressure sensor details
bmp_p = {
    "type": "Pressure",
    "location": "Basil's Room",
    "name": "unami_bmp_p",
    "unit": "hPa"  # Hectopascal unit for pressure measurement
}
# Send a POST request to register the BMP280 pressure sensor
r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_p, headers=auth)
print(f'BMP Pressure: {r.json}')  # Print the response from the server

print("Even happier")  # Indicate that all sensor registrations are complete
