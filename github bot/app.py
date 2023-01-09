from selenium import webdriver
from userinfo import username, password
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Github:


    def __init__(self):
        self.browser = webdriver.Chrome()
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get(self.baseUrl + "login")
        time.sleep(1)
        self.browser.find_element(By.ID, 'login_field').send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.NAME, "commit").click()


    def __del__(self):
        time.sleep(4)
        self.browser.close()


app = Github()

app.signIn()
# app.getFollowers()
# app.findRepositories('python')