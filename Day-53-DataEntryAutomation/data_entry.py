from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Program Files (x86)/chromedriver"
FORM_URL = "https://forms.gle/G4Zoga4RwKWBskDW8"

class DataEntry():
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()

    def write_data(self,address,price,link):
        self.driver.get(FORM_URL)
        sleep(1)
        address_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        
        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        submit_btn.click()