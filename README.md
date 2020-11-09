# BonusDeal
This is a python(Selenium)-based tool to generate the list of grocery items that are on sale (Albert Heijn, a Dutch supermarket chain). The user can use a number of  features by using command-line operation. 

Used methods:
  1) Web scraping : Python Selenium is used to retrieve necessary information from a web page. Also, automatic click and intelligent scroll are used to correctly                       gather dynamically-loaded contents.
  2) Object-oriented programming : The code is modular, and modules are separately logically. 
  3) Command-line interface : Argparse is used.

Feature :
  1) Partial search (--s) : if the user search for a name of an item, the program uses regular expression and automatically searches if this item is on sale right                                now. 
  2) Generate List (--a) : the program can provide a complete list of grocery items that are on sale right now without duplicates. 
  3) Export (--e) : the program automatically generates a txt file which includes all the items on sale.
