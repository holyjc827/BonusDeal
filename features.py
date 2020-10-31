from re import search
from main import WebScraper

class features:

    def partial_search(self):
        lookup = input("What do you want to find?: ")

        for item in WebScraper.item_list:
            if search(lookup, item):
                WebScraper.return_list.append(item)
        print(WebScraper.return_list)