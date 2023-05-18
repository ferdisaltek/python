import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/Samsung-Telefonu-Phantom-T%C3%BCrkiye-Garantili/dp/B0BSLW3NNN?ref_=Oct_d_otopr_d_13709907031_9&pd_rd_w=rn6fa&content-id=amzn1.sym.f9c17f0f-98c1-44d7-8be4-d463c414346d&pf_rd_p=f9c17f0f-98c1-44d7-8be4-d463c414346d&pf_rd_r=ZYN2AN03XA2TZ82JMB58&pd_rd_wg=SXPqg&pd_rd_r=ec482486-e06d-494f-aad7-577a999d448e&pd_rd_i=B0BSLW3NNN"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
print(price)
