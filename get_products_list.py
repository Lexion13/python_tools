import requests
from bs4 import BeautifulSoup
import time
import re

base_url = "https://www.craft-store.jp/products?page="
item_list = []

for i in range(10):
    time.sleep(1)
    url = base_url + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.select("#relative-product a")
    for item in items:
        item = item.get('href')
        item_list.append(item)

item_list = list(set(item_list))

## no item_list is the array complete include products urls. you see?
## OK let's get do that.

def get_item_and_sku(url):
    time.sleep(1)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    child_name = soup.select_one(".product-main-info h1").string
    brand = soup.select_one(".product-main-info h2").string
    #this is child information
    url = url.strip()
    print("child", brand, child_name, url, sep=",")

    skus = soup.select("#cart-form form")
    for sku in skus:
        sku_name = sku.select_one(".product-main-info-item-name").string
        sku_price = sku.select_one(".product-price").text
        sku_price = sku_price.replace(',', '')
        sku_price = re.sub("円.*", "", sku_price)
        sku_price = re.sub(".* ", "", sku_price)
        sku_price = sku_price.rstrip()
        sku_price = int(sku_price)


        sku_id = sku.select_one("#variant_sku").get("value")
        print("sku", end=",")
        print(brand, end=",")
        print(sku_name, end=",")
        print(url, end=",")
        print(sku_price, end=",")
        print(sku_id, end=",")
        print("")




for item in item_list:
    get_item_and_sku(item)
