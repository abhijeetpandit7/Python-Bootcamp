from selenium import webdriver
python_url = "https://www.python.org/"

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(python_url)

event_list = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_names = event_list.find_elements_by_css_selector("li")
events_dates = event_list.find_elements_by_css_selector("li time")
events = {}
for n in range(len(events_names)):
    events[n] = {
        'name': events_names[n].text,
        'date': events_dates[n].text
    }
print(events)

driver.quit()