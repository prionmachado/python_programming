import requests
import json

print("================= Welcome to the Weather App! ===================\n")

city = input("Enter the name of the city: ") 
url = f"http://api.weatherapi.com/v1/current.json?key=8a914c9c23f64b4690e83427252705&q={city}" 

r = requests.get(url) 

weatherdic = json.loads(r.text) 
print(f"\nCountry: {weatherdic['location']['country']}")
print(f"City: {weatherdic['location']['name']}") 
print(f"Region: {weatherdic['location']['region']}")
print(f"Temperature: {weatherdic['current']['temp_c']}°C") 
print(f"Condition: {weatherdic['current']['condition']['text']}")
print(f"Humidity: {weatherdic['current']['humidity']}%") 
print(f"Wind Speed: {weatherdic['current']['wind_kph']} kph")
print(f"Time Zone: {weatherdic['location']['tz_id']}")
print(f"Latitude: {weatherdic['location']['lat']}")
print(f"Longitude: {weatherdic['location']['lon']}\n") 