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

    response = requests.get("https://www.amazon.com.tr/Samsung-Telefonu-Phantom-T%C3%BCrkiye-Garantili/dp/B0BSLW3NNN/ref=sr_1_5?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3D71YSP57KUUJ&keywords=Samsung+Galaxy+S23+Ultra+256+GB&qid=1684434249&sprefix=samsung+galaxy+s23+ultra+256+gb%2Caps%2C101&sr=8-5")
    

    soup = BeautifulSoup(response.content, "lxml")
    print(soup.prettify())

    price = soup.find(class_="a-offscreen").get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
    
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
product_url = 'https://example.com/product'  # Replace with the actual product URL
target_price = 100  # Replace with the desired target price
current_price = get_product_price(product_url)

if float(current_price) < target_price:
    email_subject = 'Price Alert: Product Price Dropped!'
    email_body = f"The price of the product has dropped to {current_price}. You can check it at {product_url}"
    recipient_email = 'recipient_email@gmail.com'  # Replace with the recipient's email address
    
    send_email(recipient_email, email_subject, email_body)
    print("Email notification sent!")
else:
    print("Price has not dropped yet.")