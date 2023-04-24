from urllib import response
import requests


response=requests.get(url="https://api.sunrise-sunset.org/json?lat=41.035783&lng=29.225065&date=today")
print(response.status_code)
response.raise_for_status()
print(response.json())

