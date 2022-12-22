# import requests

# url="https://newsapi.org/v2/everything?q=apple&from=2022-12-21&to=2022-12-21&sortBy=popularity&apiKey=89efa6e219e647c5b9927eae3f2f4bcb"

# response=requests.get(url)

# news=response.json()
# print(news["articles"][0])


import requests

headlines_url = "https://newsapi.org/v2/top-headlines"
everything_url = "https://newsapi.org/v2/everything"

api_key = "api_key"


# response = requests.get(headlines_url, params={
#     "apiKey": api_key,
#     "country": "tr"
# })

response = requests.get(everything_url, params={
    "apiKey": api_key,
    "q": "futbol",
    "language": "tr",
    "sortBy": "publishedAt"
})

haberler = response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])