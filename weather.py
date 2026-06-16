import urllib.request
import json

def get_weather(city):
    api_key = 5966cf33bc51bddc75c15cb984ffd08e  
    city_encoded = city.replace(" ", "+")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        name        = data["name"]
        country     = data["sys"]["country"]
        temp        = data["main"]["temp"]
        feels_like  = data["main"]["feels_like"]
        humidity    = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed  = data["wind"]["speed"]

        print("\n" + "=" * 40)
        print(f"  📍 {name}, {country}")
        print("=" * 40)
        print(f"  🌡️  Temperature : {temp}°C")
        print(f"  🤔 Feels Like  : {feels_like}°C")
        print(f"  💧 Humidity    : {humidity}%")
        print(f"  💨 Wind Speed  : {wind_speed} m/s")
        print(f"  🌤️  Condition   : {description}")
        print("=" * 40 + "\n")

    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("\n❌ Invalid API key. Please check your key.\n")
        elif e.code == 404:
            print(f"\n❌ City '{city}' not found. Try again.\n")
        else:
            print(f"\n❌ Error: {e}\n")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}\n")

def main():
    print("=" * 40)
    print("   🌦️  Live Weather App")
    print("=" * 40)

    while True:
        print()
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("\n👋 Bye! Stay weather-aware!\n")
            break
        if not city:
            print("⚠️  Please enter a city name.")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()
