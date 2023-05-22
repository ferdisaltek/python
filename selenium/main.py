from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
url="https://www.amazon.com.tr/Samsung-Galaxy-Telefonu-T%C3%BCrkiye-Garantili/dp/B0BSLY99Q9/ref=sr_1_4?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=s23&qid=1684779487&s=telephone&sr=1-4"
driver.get(url)

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text )

driver.quit()