from bs4 import BeautifulSoup
import requests as rq
#import csv
from openpyxl import Workbook

search_term = 'iphone'
url = f'https://www.amazon.com.br/s?k={search_term}'

#patrocinados
#results = soup.find_all('div', class_ = 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20')
#print(results)

def getData(url):
    counter = 0
    while True:
        r = rq.get(url)
        if r.status_code == 200:
            html_txt = r.text
            soup = BeautifulSoup(html_txt, 'lxml')
            return soup
        counter += 1
        if counter == 100:
            break

def getNextPage(soup):
    page = soup.find('div', class_ = 'a-section a-text-center s-pagination-container')
    if not page.find('span', class_ = 's-pagination-item s-pagination-next s-pagination-disabled'):
        new_page = page.find('a', class_ = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator').get('href')
        url = 'https://www.amazon.com.br' + new_page
        return url
    else:
        return

def getTitle(result):
    return result.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').text

def getPrice(result):
    try:
        return result.find('span', class_ = 'a-price').find('span', class_ = 'a-offscreen').text
    except:
        return ''

def getLink(result):
    try:
        return str('https://www.amazon.com.br' + result.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').parent['href'])
    except:
        return ''

def getRating(result):
    try:
        return result.find('i', class_ = 'a-icon-star-small').text
    except:
        return ''

records = []

while url:
    soup = getData(url)
    results = soup.find_all('div', class_ = 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
    for result in results:
        
        title = getTitle(result)
        price = getPrice(result)
        rating = getRating(result)
        link = getLink(result)
        
        record =    (
                        title,
                        price,
                        rating,
                        link
                        )

        records.append(record)

    url = getNextPage(soup)

#with open('results.csv', 'w', newline='', encoding='utf-8') as f:
#    w = csv.writer(f)
#    w.writerow(['Descrição',  'Preço', 'Rating', 'Link'])
#    w.writerows(records)

wb = Workbook()
ws = wb.active
ws.append(['Descrição',  'Preço', 'Rating', 'Link'])
for record in records:
    ws.append(record)
wb.save('results.xlsx')