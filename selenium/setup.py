from selenium import webdriver

chrome_driver_path="C:/python_learn/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://google.com")

driver.close()
