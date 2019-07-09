import bs4
import pandas as pd
import requests

URL = 'https://pybit.es/pages/articles.html'

site = requests. get(URL)
site.raise_for_status()

soup = bs4.BeautifulSoup(site.text, 'html.parser')

all_li = soup.main.find_all('li')

for a, item in enumerate(all_li):
    print(a+1, item.string)


number = []
name = []

for a, item in enumerate(all_li):
    number.append(a+1)
    name.append(item.string)

df = pd.DataFrame({'no':number, 'name':name})