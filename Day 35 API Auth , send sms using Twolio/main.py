import os
import requests
from twilio.rest import Client

account_sid = "YOUR_SID"

auth_token = os.environ.get("AUTH_TOKEN")

OWM_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.environ.get("OWM_API_KEY")

weather_params = {
    # Delhi, India
    # "lat": 28.63,
    # "lon": 77.21,
    # Delhi,US
    "lat": 32.45,
    "lon": -91.49,
    "appid": API_KEY,

}

data = requests.get(url=OWM_endpoint, params=weather_params)
# print(data.url)

data.raise_for_status()
hourly_data_list = (data.json()['hourly'])

will_rain = False
for i in range(12):
    hour = hourly_data_list[i]

    if (hour['weather'][0]['id'] < 700):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain today!",
            from_='+19543711080',
            to='RECEIVER_NUMBER'
        )
    print(message.status)
