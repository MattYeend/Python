import requests  # Ensure requests is installed

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"  # API endpoint
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try: 
        response = requests.get(base_url, params=params)
        data = response.json()  # ✅ Fix: Call json() as a method

        # Check if the city is found
        if response.status_code == 200:
            city = data.get('name', 'Unknown City')
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Description: {description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"An error occurred: {e}")
