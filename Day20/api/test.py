import requests

lat = 37.491
lon = 126.72
apikey = "9f9f49703cd3a362fd91f7db5974b96b"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"
response = requests.get(url)
data = response.json()
print(data)