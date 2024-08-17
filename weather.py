import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
    else:
        return None

def display_weather(data):

    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    else:
        print("Could not retrieve weather data. Please check the location or API key you given.")


api_key = "Add your API Key here........"  

location = input("Enter the city Name or ZIP code: ")
weather_data = get_weather(api_key, location)

display_weather(weather_data)
