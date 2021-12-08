import requests
# twilio class
from twilio.rest import Client

# twilio details
account_sid = # put your account_sid of twilio here
auth_token = # put your twilio auth_toke

weather_param = {
    "lat": # put your location's latitude,
    "lon": #put your location's longitude,
    "appid": # put appid from the website,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_param)
print(response.raise_for_status())

data = response.json()

# using slicing, to get data for first 12 hours
data_sliced = data["hourly"][:12]
will_rain = False

for hour_data in data_sliced:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella!☔️")
    # send sms
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_= # put twilio generated number,
        to= # put receiver's phone number
    )
    print(message.status)