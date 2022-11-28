# Assignment 12.1
import requests
import json
import requests

try:
    request = "https://api.chucknorris.io/jokes/random?category=dev"
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print(f"No response, reason: HTTP meow error.")

# Assignment 12.2
API_KEY = 'API-KEY'
city = input("Enter a city name: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}"

def K_C(temp_k):
    return round(temp_k - 273.15, 1)

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(json.dumps(json_response, indent=1))
        cur_tmp = json_response["main"]["temp"]
        cur_weather = json_response["weather"][0]["description"]
        cur_weather_feels = json_response["main"]["feels_like"]
        print(f"Currently it is {cur_weather} in {city} with temperature {K_C(cur_tmp)} C. "
              f"\nFeels like {K_C(cur_weather_feels)} C.")
except requests.exceptions.RequestException as e:
    print("Request could not be completed")
