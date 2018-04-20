import re
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.craft-store.jp/products/suginokicraft_lunchbox"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

title = soup.select_one(".product-main-info h1").string
brand = soup.select_one(".product-main-info h2").string
description = soup.find(attrs={"name": "description"})
description = description['content']
print(title)
print(brand)
print(description)
price_list = []

prices = soup.select(".product-price")
for price in prices:
    price = price.text
    price = re.sub(",|円.*" , '', price)
    price = price.strip()
    price = int(price)
    print(price)
    price_list.append(price
mn_price = min(price_list)
mn_price = "{:,}".format(mn_price)

images = []
imgs = soup.select(".product-main-info-image img")
for img in imgs:
    img = img['src']
    images.append(img)

img = images[0]

top_images = soup.select("#slick img")
top_image = top_images[0]
top_image = top_image['src']

'''
top_image
img
mn_price
description
title
brand
'''


print('''
<img src="{0}" class="img-responsive">
<div class="row item-foreword2-wrap">
    <div class="col-xs-12 col-sm-7 col-md-7">
        <p>{1}</p>
    </div>

    <div class="col-xs-12 col-sm-5 col-md-5">
        <div class="row">
            <div class="col-xs-5 item-foreword2-image">
                <img src="{2}" class="img-responsive">
            </div>
            <div class="col-xs-7">
                <p class="item-foreword2-brand">{3}</p>
                <p class="item-foreword2-item-name">{4}</p>
                <p class="item-foreword2-price">{5}円&nbsp;(税込／送料別)</p>
            </div>
            <div class="col-xs-12">
                <a class="item-foreword2-btn" href="{6}">ご購入はこちら</a>
            </div>
        </div>
    </div>

</div>
'''.format(top_image,description,img,brand,title,mn_price,url))

