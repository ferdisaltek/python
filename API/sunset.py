from urllib import response
import requests


response=requests.get(url="https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today")
print(response.status_code)
response.raise_for_status()
print(response.json())

