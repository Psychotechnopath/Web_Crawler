from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re

url = "https://www.plus500.nl/Instruments/BTCUSD"

req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

page_html = urlopen(req).read()
page_soup = soup(page_html, 'html.parser')

match = re.search('SellPrice: \'(.*)\',\r\n', str(page_soup))
price = match.group(1) if match else None
print(price)