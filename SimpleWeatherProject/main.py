from Python.SimpleWeatherProject.weather import get_weather
from Python.SimpleWeatherProject.config import API_KEY

def main():
    print("Welcome to the Weather App!")
    city_name = input("Enter the name of a city: ")

    # Fetch and display the weather data
    get_weather(city_name, API_KEY)

if __name__ == "__main__": 
    main()