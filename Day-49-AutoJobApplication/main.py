import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
load_dotenv()

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
linkedIn_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
job_application_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer&sortBy=R"

driver.get(linkedIn_url)
email_input = driver.find_element_by_name("session_key")
email_input.send_keys(os.getenv("email"))
password_input = driver.find_element_by_name("session_password")
password_input.send_keys(os.getenv("password")+Keys.ENTER)

driver.get(job_application_url)
sleep(2)
job_list = driver.find_elements_by_class_name("jobs-search-results__list-item")

for job_application in job_list:
    job_application.find_element_by_css_selector("div div div a").click()
    sleep(1)
    apply_btn = driver.find_element_by_class_name("jobs-apply-button")
    apply_btn.click()
    button = driver.find_elements_by_class_name("artdeco-button--primary")[0]

    if button.get_attribute("aria-label")=="Submit application":
        mobile_input = driver.find_element_by_css_selector("div.display-flex input.fb-single-line-text__input")
        mobile_input.send_keys(os.getenv('mobile'))
        button.click()
    else:
        dismiss_btn = driver.find_element_by_class_name("artdeco-modal__dismiss")
        dismiss_btn.click()
        discard_btn = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
        discard_btn.click()