import requests # Will need to install requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather" # Will need an account with openweathermap
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" # Use "imperial" for fahrenheit
    }

    try: 
        response = requests.get(base_url, params=params)
        data = response.json

        # Check if the city is found
        if response.status_code == 200:
            city = data['name']
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}˚C")
            print(f"Description: {description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")