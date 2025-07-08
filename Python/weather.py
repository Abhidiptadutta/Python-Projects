import requests

city = "Kolkata"
api_key = "demo"  # Replace with your OpenWeather API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


res = requests.get(url)
data = res.json()

if res.status_code == 200:
    print(f"Weather in {city}: {data['main']['temp']}°C")
else:
    print("Error fetching weather data.")
