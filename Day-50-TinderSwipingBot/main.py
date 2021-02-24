import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
tinder_url = "https://tinder.com/"

driver.get(tinder_url)
sleep(5)

try:
    accept_cookies = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[2]/div/div/div[1]/button')
    accept_cookies.click()
except NoSuchElementException:
    pass

login_btn = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_btn.click()

sleep(3)
try:
    login_with_facebook_btn = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
except NoSuchElementException:
    more_options = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
finally:
    login_with_facebook_btn = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_with_facebook_btn.click()
    sleep(5)

## In Selenium, each window has a identification handle, we can get all the window handles with:
# driver.window_handles
base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]

# # Switch to popup login window
driver.switch_to.window(facebook_login_window)
# # Can verify by printing driver title
# print(driver.title)

email_input = driver.find_element_by_name("email")
email_input.send_keys(os.getenv("email"))
password_input = driver.find_element_by_name("pass")
password_input.send_keys(os.getenv("password")+Keys.ENTER)

driver.switch_to.window(base_window)

sleep(10)
try:
    allow_location_btn = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[1]')
    allow_location_btn.click()
except NoSuchElementException:
    pass
sleep(5)
try:
    disable_notif_btn = driver.find_element_by_xpath('//*[@id="t--1700653258"]/div/div/div/div/div[3]/button[2]')
    disable_notif_btn.click()
except NoSuchElementException:
    pass

#Tinder free tier only allows 100 "Likes" per day. 
for n in range(100):
    sleep(1)
    try:
        like_btn = driver.find_element_by_xpath('//*[@id="t-339552546"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()
    except NoSuchElementException:
        sleep(2)