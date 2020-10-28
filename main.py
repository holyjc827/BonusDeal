from selenium import webdriver
import math
import time

PATH = "/Users/jcpark/Desktop/Coding/WebScraping/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ah.nl/bonus")
item_list = []

button = driver.find_element_by_id("accept-cookies")
button.click()

scrollHeight = driver.execute_script("return document.body.scrollHeight")
for i in range(1, math.ceil(scrollHeight / 1000)):
    driver.execute_script("window.scrollTo(" + str((i - 1) * 1000) + "," + str(i * 1000) + ")")
    time.sleep(0.5)

try:
    items = driver.find_elements_by_class_name("link_root__2DsAD")
    for item in items:
        name = item.get_attribute("title")
        item_list.append(name)
    item_list = list(dict.fromkeys(item_list))
    print(item_list)
except:
    driver.quit()