import http.client

conn = http.client.HTTPSConnection("inteltech.p.rapidapi.com")

payload = "sms=%2B905051111111&message=Test%20message%20here.&senderid=MyCompany&key=ertgertert-aaaa-ssss-ffff-dsdfasdf&username=xxxx"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "your_api_key",
    'X-RapidAPI-Host': "inteltech.p.rapidapi.com"
    }

conn.request("POST", "/send.php", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))