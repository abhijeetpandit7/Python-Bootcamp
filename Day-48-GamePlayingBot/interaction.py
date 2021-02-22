from selenium import webdriver
from selenium.webdriver.common.keys import Keys
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
newsletter_url = "https://flightdeals.herokuapp.com/"

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(newsletter_url)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
fName_input = driver.find_element_by_name("fname")
lName_input = driver.find_element_by_name("lname")
email_input = driver.find_element_by_name("email")
submit_btn = driver.find_element_by_css_selector("form button")

fName_input.send_keys("Abhijeet")
lName_input.send_keys("Pandit")
email_input.send_keys("abhijeetpandit233@gmail.com"+Keys.ENTER)
# submit_btn.click()

# driver.close()