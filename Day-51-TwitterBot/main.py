import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
load_dotenv()
TWITTER_URL = "https://twitter.com/login"
OOKLA_URL = "https://www.speedtest.net/run"
PROMISE_DOWN = 30
PROMISE_UP = 10
chrome_driver_path = "/Program Files (x86)/chromedriver"

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.ACTUAL_DOWN = 0
        self.ACTUAL_UP = 0
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get(OOKLA_URL)
        sleep(60)
        self.ACTUAL_DOWN = float(self.driver.find_element_by_class_name("download-speed").text)
        self.ACTUAL_UP = float(self.driver.find_element_by_class_name("upload-speed").text)
        if(self.ACTUAL_DOWN<PROMISE_DOWN or self.ACTUAL_UP<PROMISE_UP):
            self.tweet_at_provider()
    
    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(3)
        email_input = self.driver.find_element_by_name("session[username_or_email]")
        password_input = self.driver.find_element_by_name("session[password]")
        email_input.send_keys(os.getenv("EMAIL"))
        password_input.send_keys(os.getenv("PASSWORD")+Keys.ENTER)
        sleep(3)
        tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.ACTUAL_DOWN}down/{self.ACTUAL_UP}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up?")
        sleep(3)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()