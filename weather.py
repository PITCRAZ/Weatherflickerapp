import requests

weather_Api_Key = "3236efad6f850917b6fe4acb9137bec8"

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_Api_Key}&units=imperial"

    response = requests.get(url)

    if response.status_code == 200:
        print("Weather data retrieved successfully.")
        ##print(response.json())
        print("Temperature:", response.json()['main']['temp'], "°F")
        print("Weather Description:", response.json()['weather'][0]['description'])
        print("Humidity:", response.json()['main']['humidity'], "%")
        print("City:", response.json()['name'])
        return response.json()

    else:
        return None

get_weather(40.7128, -74.0060)



