from lib2to3.pgen2 import driver
from selenium import webdriver
import time

driver=webdriver.Chrome()
url="https://www.github.com/"
driver.get(url)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("selenium/github.png")
time.sleep(3)
driver.get(url+"name")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

driver.close()