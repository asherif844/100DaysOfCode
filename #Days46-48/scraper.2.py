import bs4
import pandas as pd
import requests

mainURL = 'https://www.mycomicshop.com/newreleases'


def get_page_count(url):
    site = requests.get(url)
    site.raise_for_status()

    soup = bs4.BeautifulSoup(site.text, 'html.parser')

    all_li = soup.find_all('li')

    numbers_list = []

    for item in all_li:
        a = item.string
        numbers_list.append(a)

    numbers = []
    for i in numbers_list:
        try:
            # print(int(i))
            numbers.append(int(i))
        except:
            continue

    return min(numbers), max(numbers)

max_page_count = get_page_count(mainURL)[1]





def printComicBooks(page_count):
    comic_list = []    

    for i in range(page_count+1):
        pageUrl = f'https://www.mycomicshop.com/newreleases?dw=0&p={i}'        
        page = requests.get(pageUrl)
        page.raise_for_status()

        bsoup = bs4.BeautifulSoup(page.text, 'html.parser')
        all_titles = bsoup.find_all('div', class_ = 'title')
        for i in all_titles:
            comic_name = i.a.text
            comic_number = i.strong.text
            comic = f'{comic_name}: {comic_number}'
            comic_list.append(comic)
    return set(comic_list)

listOfComics = list(printComicBooks(max_page_count))

for i in listOfComics:
    # print(i.split(':'))
    print(i.split('(', 1)[1].split(')')[0])
