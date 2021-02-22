from selenium import webdriver
amazon_url = "https://www.amazon.in/Fossil-Neutra-Chrono-Analog-Black/dp/B07CGRCJG3/ref=sr_1_32?crid=SCJBM1YN90HW&dchild=1&keywords=watch+for+men&qid=1613923319&refinements=p_n_feature_fourteen_browse-bin%3A11142592031%2Cp_n_feature_seven_browse-bin%3A1480900031%2Cp_n_feature_sixteen_browse-bin%3A15752672031%7C5756155031&rnid=5756152031&s=watches&sprefix=wat%2Caps%2C314&sr=1-32"
python_url = "https://www.python.org/"

chrome_driver_path = "/Program Files (x86)/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(python_url)

# Find element

# price = driver.find_element_by_id("priceblock_ourprice")

# searchbar = driver.find_element_by_name("q")
# tag_name = searchbar.tag_name
# attribute = searchbar.get_attribute("placeholder")

# logo = driver.find_element_by_class_name("python-logo")

# link = driver.find_element_by_css_selector(".documentation-widget a")

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

## Closes a tab
# driver.close()
# Closes window
driver.quit()