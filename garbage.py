import requests
from bs4 import BeautifulSoup
import time


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

domain = "https://www.zerokarabitcoin.com/"

google = "https://www.google.co.jp/search?q="

headline = "仮想通貨"


sitecmdurl = google + "site:" + domain + " " + headline
r = requests.get(sitecmdurl, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find_all("a")
ss = soup.select_one("#search h3 a").get('href')
print(ss)