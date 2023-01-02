from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.n11.com/urun/xiaomi-12t-pro-12-gb-256-gb-xiaomi-turkiye-garantili-25968120?magaza=exbilisim")

title = driver.find_element_by_class_name("proName").text
price = driver.find_element_by_class_name("newPrice").find_element_by_tag_name("ins").text
searchInput = driver.find_element_by_id("searchData").get_attribute("value")
link = driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div[2]/div/ul/li[2]/a').get_attribute("href")
logo = driver.find_element_by_css_selector(".logo img").get_attribute("src")
print(title)
print(price)
print(searchInput)
print(link)
print(logo)

driver.close()