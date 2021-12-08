# RainAlert

Project Name : Rain Alert SMS Generator

Author : Gulafsha Ahmed

Language : Python

This project aims at checking the weaher conditions of the entered location(in main.py). If it is going to rain on that particular day, a programmatically generated message using Twilio will be sent to receiver's phone number alerting the person to carry an umbrella! The project also makes use of requests module of python.

main.py : contains the functionality of the project. The variables account_sid and auth_token need to be initialised with user's twilio details respectively. User also needs to put the latitude and longitude of the user's location. This can be easily found at https://www.latlong.net. An appid generated at https://api.openweathermap.org also needs to be put against "appid" key in the weather_param dictionary. The reciver's phone number also needs to be added in main.py.
