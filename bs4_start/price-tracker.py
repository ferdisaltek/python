import requests
from bs4 import BeautifulSoup
import smtplib

def get_product_price(url):
    # # Send a GET request to the website
    # response = requests.get("https://www.amazon.com.tr/Samsung-Telefonu-Phantom-T%C3%BCrkiye-Garantili/dp/B0BSLW3NNN/ref=sr_1_5?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3D71YSP57KUUJ&keywords=Samsung+Galaxy+S23+Ultra+256+GB&qid=1684434249&sprefix=samsung+galaxy+s23+ultra+256+gb%2Caps%2C101&sr=8-5")
    
    # # Create a BeautifulSoup object to parse the HTML content
    # soup = BeautifulSoup(response.content, 'html.parser')
    

    # # Find the element containing the price
    # price_element = soup.find('span', class_='a-offscreen')
    # print(price_element)
    # # Extract the price value
    # price = price_element.text.strip()

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
    
    return price

def send_email(to_address, subject, body):
    # Replace these with your own email and password
    from_address = 'your_email@gmail.com'
    password = 'your_email_password'
    
    # Create a secure connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    
    # Compose the email message
    message = f"Subject: {subject}\n\n{body}"
    
    # Send the email
    server.sendmail(from_address, to_address, message)
    
    # Close the connection
    server.quit()

# Example usage
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )