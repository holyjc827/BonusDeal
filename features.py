from re import search

class features:

    def partial_search(self, item_list, return_list):
        search_word = input("What do you want to find?: ")

        for item in item_list:
            if search(search_word, item):
                return_list.append(item)

        if len(return_list) > 0:
            return print(return_list)
        else:
            print("This item is not on sale this week")

    def return_complete_list(self, item_list):
        return print(item_list)

    def export_list(self, item_list):
        with open('list.txt','w') as l:
            l.writelines("%s\n" % item for item in item_list)
