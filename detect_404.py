import requests
from bs4 import BeautifulSoup
import time

urls = [
    "https://www.zerokarabitcoin.com",
    "https://www.zerokarabitcoin.com/entry/ranking",
    "https://www.zerokarabitcoin.com/entry/amanatsu",
    "https://www.zerokarabitcoin.com/entry/exchange2",
    "https://www.zerokarabitcoin.com/entry/zaiftsumitate",
    "https://www.zerokarabitcoin.com/entry/mona",
    "https://www.zerokarabitcoin.com/sitemap",
    "https://www.zerokarabitcoin.com/entry/cryptocurrency",
    "https://www.zerokarabitcoin.com/entry/bitcoin",
    "https://www.zerokarabitcoin.com/entry/bitbank",
    "https://www.zerokarabitcoin.com/entry/btcbitflyer",
    "https://www.zerokarabitcoin.com/entry/sbibank",
    "https://www.zerokarabitcoin.com/entry/binance",
    "https://www.zerokarabitcoin.com/entry/dmmbitcoin",
    "https://www.zerokarabitcoin.com/entry/binanceapp",
    "https://www.zerokarabitcoin.com/entry/kucoin",
    "https://www.zerokarabitcoin.com/entry/ripplexrp",
    "https://www.zerokarabitcoin.com/entry/coincheckbitcoin",
    "https://www.zerokarabitcoin.com/entry/send",
    "https://www.zerokarabitcoin.com/entry/app",
    "https://www.zerokarabitcoin.com/entry/coincheckmargin",
    "https://www.zerokarabitcoin.com/entry/change2fa",
    "https://www.zerokarabitcoin.com/entry/gmocoin",
    "https://www.zerokarabitcoin.com/page/2",
    "https://www.zerokarabitcoin.com/page/4",
    "https://zaif.jp?ac=hjh8dspk97",
    "https://bitflyer.jp?bf=efbzb3qc",
    "https://p-salm.jp/ad/p/r?_site=72&_article=3&_link=4&_image=4",
    "https://p-salm.jp/ad/p/r?_site=72&_article=8&_link=14&_image=14",
    "https://twitter.com/kakip_21",
    "https://feedly.com/i/subscription/feed/https://www.zerokarabitcoin.com/feed",
    "https://www.zerokarabitcoin.com/entry/category/%e3%82%a2%e3%83%ab%e3%83%88%e3%82%b3%e3%82%a4%e3%83%b3",
    "https://www.zerokarabitcoin.com/entry/category/%e3%82%a6%e3%82%a9%e3%83%ac%e3%83%83%e3%83%88",
    "https://www.zerokarabitcoin.com/entry/category/%e3%82%bb%e3%82%ad%e3%83%a5%e3%83%aa%e3%83%86%e3%82%a3",
    "https://www.zerokarabitcoin.com/entry/category/bitcoin",
    "https://www.zerokarabitcoin.com/entry/category/bitcoin/%e4%b8%96%e3%81%ae%e4%b8%ad",
    "https://www.zerokarabitcoin.com/entry/category/%e5%88%9d%e5%bf%83%e8%80%85%e5%90%91%e3%81%91",
    "https://www.zerokarabitcoin.com/entry/category/%e5%8f%96%e5%bc%95%e6%89%80",
    "https://www.zerokarabitcoin.com#container",
    "https://www.zerokarabitcoin.com/entry/coincheck",
    "https://www.zerokarabitcoin.com/entry/wallet",
    "https://www.zerokarabitcoin.com/entry/tag/bitcoin",
    "https://www.zerokarabitcoin.com/entry/tag/dash",
    "https://www.zerokarabitcoin.com/entry/tag/ethereum",
    "https://www.zerokarabitcoin.com/entry/tag/ethereum-classic",
    "https://www.zerokarabitcoin.com/entry/tag/factom",
    "https://www.zerokarabitcoin.com/entry/tag/litec",]





def detect404(url):
    r = requests.get(url)
    print(url, r)
for url in urls:
    detect404(url)

