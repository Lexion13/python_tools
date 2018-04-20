import requests
from bs4 import BeautifulSoup
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Please set domain below
domain = "https://www.zerokarabitcoin.com/"

google = "https://www.google.co.jp/search?q="

urls =[
"https://www.zerokarabitcoin.com/entry/bitcoin-hardfork-shikumi-kongo",
"https://www.zerokarabitcoin.com/entry/monacoin-kongo"
]

def get_site_command_result(headline):
    sitecmdurl = google + "site:" + domain + " " + headline
    r = requests.get(sitecmdurl, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("a")
    ss = soup.select_one("#search h3 a").get('href')
    ss = re.sub("&.*", "", ss)

    return ss


def detect_headlines(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines2 = soup.select(".entry-content h2")
    headlines3 = soup.select(".entry-content h3")
    headlines = headlines2 + headlines3
    for headline in headlines:
        headline = headline.text
        result = get_site_command_result(headline)
        print(url, headline, result, sep=',')


for url in urls:
    detect_headlines(url)


