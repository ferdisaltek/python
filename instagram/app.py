from selenium import webdriver
from userinfo import username, password
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class Instagram:

 
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.NAME,'username')
        passwordInput = self.browser.find_element(By.NAME,'password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(4)

        if self.browser.find_element(By.CLASS_NAME, 'cmbtv'):
            el = self.browser.find_element(By.CLASS_NAME,'cmbtv')
            el.find_element(By.TAG_NAME,'button').click()

        time.sleep(4)

        if self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'):
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def getFollowers(self):
        pass

    def followUser(self, username):
        pass

    def unFollowUser(self, username):
        pass

    def __del__(self):
        time.sleep(10)
        # self.browser.close()

app = Instagram(username, password)

app.signIn()
app.getFollowers()
app.followUser('abc')
app.unFollowUser('abc')