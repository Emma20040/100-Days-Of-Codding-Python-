import requests

OWN_endpoint =" https://api.openweathermap.org/data/2.5/onecall"

api_key ="3579085631ee1948007be6ddad5bb455"
weather_params ={
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current, minutely,daily"
}

response = requests.get(OWN_endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print(weather_data)