from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
game_url = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(game_url)
cookie = driver.find_element_by_id("bigCookie")
sleep(2)
store_products = driver.find_elements_by_css_selector("div#products div.product")
store_products = store_products[::-1]
minute_timer = time() + 60*5

while time()<minute_timer:
    seconds_timer = time() + 5
    while time()<seconds_timer:
        cookie.click()
    for product in store_products:
        if 'enabled' in product.get_attribute("class"):
            product.click()

cookies_per_second = driver.find_element_by_id("cookies").text
print(f"Cookies per second: {cookies_per_second.split(' ')[-1]}")