# import requests
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response.status_code)
# # print(response.ok)
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)
#
#

import requests
from datetime import datetime

MY_LAT = 28.693600
MY_LNG = 77.281120
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
data = (response.json())
print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)
