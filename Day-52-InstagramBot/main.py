import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

chrome_driver_path = "/Program Files (x86)/chromedriver"
instagram_url = "https://www.instagram.com/"
TARGET_ACCOUNT = "chefsteps"
FOLLOW_LIMIT = 50

class InstaFollower:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.HEIGHT = 54
        
    def login(self):
        self.driver.get(instagram_url)
        sleep(3)
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        username_input.send_keys(os.getenv("EMAIL"))
        password_input.send_keys(os.getenv("PASSWORD")+Keys.ENTER)
        sleep(3)
    
    def find_followers(self):
        self.driver.get(instagram_url+TARGET_ACCOUNT)
        show_followers = self.driver.find_element_by_partial_link_text("followers")
        show_followers.click()
        sleep(1)
        self.modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
#         for i in range(20):
#             #In this case we're executing some Javascript, that's what the execute_script() method does. 
#             #The method can accept the script as well as a HTML element. 
#             #The modal in this case, becomes the arguments[0] in the script.
#             #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
#             self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
        
    def follow(self):
        for i in range(1,FOLLOW_LIMIT):
            try:
                follow_btn = self.driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button")
            except NoSuchElementException:
                follow_btn = self.driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button")
            if follow_btn.text == 'Follow':
                follow_btn.click()
                sleep(1)
            self.driver.execute_script(f"arguments[0].scrollTop = {self.HEIGHT}", self.modal)
            if i>3: self.HEIGHT += 54

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()