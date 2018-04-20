import requests
from bs4 import BeautifulSoup
import time


domain = "tatujin-dejimono.com"
urls =[
"https://tatujin-dejimono.com/virtual_currency/minergate/",
]


for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")
    for link in links:
        print(link)

