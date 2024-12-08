import requests


# Server and user details
server_ip = "192.168.4.137"
user = {'username':'UNANDI','password':'nananandi08'}
# register (only one)
#answer = requests.post(f'http://{server_ip}/register',json=user)


login_response = requests.post(f'http://{server_ip}/login', json=user)
cookie = login_response.json().get('access_token')
if not cookie:
    raise ValueError("Failed to retrieve access token. Check login credentials.")

#fetch data from sensor
headers = {'Authorization': f'Bearer {cookie}'}
request = requests.get(f'http://{server_ip}/readings', headers=headers)
data = request.json()

#store values
readings = data['readings'][0]
dht_temp = [r["value"] for r in readings if r["sensor_id"] == 371]
dht_hum = [r["value"] for  r in readings if r["sensor_id"] == 372]
bme_temp = [r["value"] for r in readings if r["sensor_id"] == 374]
bme_hum = [r["value"] for  r in readings if r["sensor_id"] == 375]
bme_hpa = [r["value"] for  r in readings if r["sensor_id"] == 378]

print(f'BME Data Response:\n Temp: {bme_temp}\n Humidity: {bme_hum}\n Pressure: {bme_hpa}', )
print(f'DHT Data Response:\n Temp: {dht_temp}\n Humidity: {dht_hum}', )

