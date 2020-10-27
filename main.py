from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/jcpark/Desktop/Coding/WebScraping/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ah.nl/bonus")
item_list = []

# button = driver.find_element_by_id("all")
# button.click()

try:
    # main = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "page"))
    # )
    time.sleep(30)
    items = driver.find_elements_by_class_name("link_root__2DsAD")
    for item in items:
        name = item.get_attribute("title")
        item_name = {
            'name' : name
        }

        item_list.append(item_name)
        print(item_list)
except:
    driver.quit()