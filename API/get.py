from urllib import response
import requests


response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()
iss=response.json()
longitude_data=iss["iss_position"]["longitude"]
latitude_data=iss["iss_position"]["latitude"]
print(longitude_data,latitude_data)
data=(latitude_data,longitude_data)
print(data)