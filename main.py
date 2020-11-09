from selenium import webdriver
import math, time, features, argparse

f = features.features()

class WebScraper:

    def __init__(self):
        self.PATH = "/Users/jcpark/Desktop/Coding/WebScraping/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.item_list = []
        self.return_list = []

    def load(self):
        self.driver.get("https://www.ah.nl/bonus")

    def cookie_button_click(self):  # Click "Accept Cookie" button automatically
        button = self.driver.find_element_by_id("accept-cookies")
        button.click()

    def auto_scroll_bottom(self):
        # Calculate the height of the element 'body'
        scrollHeight = self.driver.execute_script("return document.body.scrollHeight")
        print(scrollHeight)
        for i in range(0, math.ceil(scrollHeight / 1000)+1):
            # Slowly scroll down to the bottom of the page to load the dynamic contents.
            self.driver.execute_script("window.scrollTo(" + str((i - 1) * 1000) + "," + str(i * 1000) + ")")
            time.sleep(0.5)

    def get_list(self):
        try:
            items = self.driver.find_elements_by_class_name("link_root__2DsAD")
            for item in items:
                name = item.get_attribute("title")
                self.item_list.append(name)
            self.item_list = list(dict.fromkeys(self.item_list))  # remove duplicates in the list.

        except:
            self.driver.quit()

    def search(self):
        f.partial_search(self.item_list, self.return_list)

    def complete_list(self):
        f.return_complete_list(self.item_list)

    def export(self):
        f.export_list(self.item_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a list of grocery that is on sale')
    parser.add_argument('--s', action='store_const', const="search")
    parser.add_argument('--a', action="store_const", const="complete")
    parser.add_argument('--e', action="store_const", const="export")
    args = parser.parse_args()

    app = WebScraper()
    app.load()
    app.cookie_button_click()
    app.auto_scroll_bottom()
    app.get_list()

    if args.s:
        app.search()
    elif args.a:
        app.complete_list()
    elif args.e:
        app.export()
