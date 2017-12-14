
import requests
from bs4 import BeautifulSoup
import time

'''
set base link

set checked_links
set check_links

check only anchor tags
get anchor tags
'''
check_links = []
checked_links = []
def get_links(url):
    if url not in checked_links:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a")
        for link in links:
            link = link.get("href")
            link = str(link)
            if "http" in link:
                link = link
            else:
                link = base_url + link

            if link not in check_links:
                check_links.append(link)
        checked_links.append(url)
    time.sleep(1)


base_url = "https://www.craft-store.jp"
get_links(base_url)

for url in check_links:
    try:
        get_links(url)
        check_links = list(set(check_links))
    except:
        print("except")



for link in checked_links:
    print(link)

for link in check_links:
    print(link)

