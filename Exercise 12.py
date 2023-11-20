# -1
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        joke_text = json_response["value"]
        print("Chunk Norris Joke:")
        print(joke_text)
    else:
        print("Failed to fetch Chuck Norris joke. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Request cannot be performed.", e)

# -2

import requests
import json

def convert_temp(k_degrees):
    c_degrees = k_degrees - 273.15
    return c_degrees


API_key = ""
city = input(" Enter a city name:")


request ="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+API_key

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        weather_description = json_response["weather"][0]["description"]
        print(f"The weather in {city} now is {weather_description}.")
        k_degrees = json_response["main"]["temp"]
        c_degrees = convert_temp(k_degrees)
        print(f"The temperature of {city} is {c_degrees}C.")
except requests.exceptions.RequestException as a:
    print("Request cannot be performed.", a)


