# importing libraries
import time
import urllib.request

from bs4 import BeautifulSoup

url = "http://services.runescape.com/m=itemdb_oldschool/viewitem?obj="


item_list = []

for i in range(400, 450):
    try:
        page = urllib.request.urlopen(url + str(i))
        print("Requesting page " + url + str(i))
        soup = BeautifulSoup(page, 'html.parser')
        item_list.append(soup.title)
        time.sleep(1)
    except urllib.error.HTTPError:
        print("Bad request")

for i in item_list:
    if str(i) == "<title>RuneScape Oldschool - Grand Exchange - Prices, Trade, Market Movers</title>":
        continue
    else:
        print(i + item_list.index(object))



