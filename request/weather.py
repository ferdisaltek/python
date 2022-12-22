import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "376bca577bcd4f81948185359222212"

sehir = input("şehir: ")

response = requests.get(url, params= {
    "key": access_key,
    "q": sehir,
    "lang": "tr"
})

sonuc = response.json()

sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havadurumu} derece ve {text}.")
