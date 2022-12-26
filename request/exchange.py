import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers= {
  "apikey": "tuOWXVNpWHhKXI10wNtZw6lsFDZQx4H8"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text