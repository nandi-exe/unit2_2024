import requests
server_ip = "192.168.4.137"
user = {'username':'UNANDI','password':'nananandi08'}
answer = requests.post(f'http://{server_ip}/login',json = user)
print(answer.json())
print("happy")
login_response = requests.post(f'http://{server_ip}/login', json=user)
cookie = login_response.json().get('access_token')
if not cookie:
    raise ValueError("Failed to retrieve access token. Check login credentials.")

auth = {'Authorization': f'Bearer {cookie}'}
#request = requests.get(f'http://{server_ip}/readings', headers=headers)


dht_t = {"type": "Temperature",
        "location": "Basil's Room",
        "name": "unami_dht_t",
        "unit": "C"} #id: tbd
r = requests.post(f'http://{server_ip}/sensor/new', json=dht_t, headers=auth)
print(f'DHT Temperature: {r.json}')

dht_h = {"type": "Humidity",
        "location": "Basil's Room",
        "name": "unami_dht_h",
        "unit": "%"} #id: tbd

r = requests.post(f'http://{server_ip}/sensor/new', json=dht_h, headers=auth)
print(f'DHT Humidity: {r.json}')

bmp_t = {"type": "Temperature",
        "location": "Basil's Room",
        "name": "unami_bmp_t",
        "unit": "C"} #id: tbd

r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_t, headers=auth)
print(f'BMP Temperature: {r.json}')


bmp_h = {"type": "Humidity",
        "location": "Basil's Room",
        "name": "unami_bmp_h",
        "unit": "%"} #id: tbd

r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_h, headers=auth)
print(f'BMP Humidity: {r.json}')

bmp_p = {"type": "Pressure",
        "location": "Basil's Room",
        "name": "unami_bmp_p",
        "unit": "hPa"} #id: tbd
r = requests.post(f'http://{server_ip}/sensor/new', json=bmp_p, headers=auth)
print(f'DHT Pressure: {r.json}')

print("Even happier")
