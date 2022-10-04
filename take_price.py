import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://steamcommunity.com/market/listings/440/Mann%20Co.%20Supply%20Crate%20Key'

response = requests.get(url)

soup = BeautifulSoup(response.text)

valueItemMarket = soup.find('span', {'class': 'market_commodity_orders_header_promote'}).get_text()
print(valueItemMarket)
#print(valor_item.prettify())
#print(valor_item.text)
#print(valueItem)