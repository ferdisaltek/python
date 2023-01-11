from webbrowser import get
from userinfo import username, password
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

class Github:


    def __init__(self):
        self.browser = webdriver.Chrome()
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get(self.baseUrl + "login")

        self.browser.find_element(By.ID, 'login_field').send_keys(self.username)
        self.browser.find_element(By.ID, "password").send_keys(self.password)

        self.browser.find_element(By.NAME, "commit").click()


    def findRepository(self,keyword):
        self.browser.get(self.baseUrl)
        searchInput=self.browser.find_element(By.NAME,"q")
        searchInput.send_keys(keyword)
        searchInput.send_keys(Keys.ENTER)

        #print(self.browser.page_source)

        repos=self.browser.find_elements(By.CSS_SELECTOR,".repo-list-item")
        #print(repos)
        for repo in repos:
            anchor = repo.find_elements(By.TAG_NAME,"a")[0]
            paragraf = repo.find_elements(By.TAG_NAME,"p")[0]
            repoName = anchor.text
            repoLink = anchor.get_attribute('href')
            description = paragraf.text

            r = {
                "name": repoName,
                "link": repoLink,
                "description": description
            }

            print(r)

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')

        for item in items:
            name = item.find_elements_by_tag_name('div')[1].find_elements_by_tag_name('span')[0].text
            username = item.find_elements_by_tag_name('div')[1].find_elements_by_tag_name('span')[1].text
            user = {
                "name": name,
                "username": username
            }
            self.followers.append(user)

    def getFollowers(self):
        self.browser.get(f"{self.baseUrl}{self.username}?tab=followers")
        self.loadFollowers()        

        while True:
            links = self.browser.find_element_by_class_name('pagination').find_elements_by_tag_name('a')

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    self.loadFollowers() 
                else:
                    break
            else:
                for link in links:
                    if  link.text == "Next":
                        link.click()
                        self.loadFollowers()
                    else:
                        continue

        print(self.followers)
        print(len(self.followers))

    def __del__(self):
        time.sleep(4)
        self.browser.close()


app = Github()

#app.signIn()
#app.getFollowers()
#app.findRepository('python')
app.getFollowers()