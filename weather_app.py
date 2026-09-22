import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("\n--- Weather Report ---")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"].title())


while True:
    city = input("\nEnter city name (or q to quit): ").strip()

    if city.lower() == "q":
        break

    try:
        get_weather(city)
    except requests.exceptions.RequestException:
        print("Unable to fetch weather. Check your city name or API key.")

