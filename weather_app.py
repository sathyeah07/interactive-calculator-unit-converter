import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key not configured.")
    exit()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        print("Unable to get weather data.")
        return

    data = response.json()

    print("\n🌤️ Weather Report")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"].title())


while True:
    city = input("\nEnter city name (or q to quit): ").strip()

    if city.lower() == "q":
        break

    get_weather(city)
