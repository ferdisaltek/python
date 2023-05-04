from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

from selenium import webdriver

chrome_driver_path="C:/python_learn/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://google.com")

driver.close()


browser.get("https://www.google.com")
print("Page title was '{}'".format(browser.title))
