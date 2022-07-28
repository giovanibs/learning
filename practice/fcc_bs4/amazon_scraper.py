import requests as rq
from bs4 import BeautifulSoup
from openpyxl import Workbook

SEARCH_TERMS = 'iphone'
url = f'https://www.amazon.com.br/s?k={SEARCH_TERMS.replace(" ", "+")}'

NO_PRICE = 1
# 0 -> não pega resultados sem preço
# 1 -> pega resultados sem preço

def getData(url):

    # contador para tentar de novo quando der erro na página
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
    # verifica se o botão de próxima página está ativo a fim de pegar o link da próxima página
    if not soup.find('span', class_ = 's-pagination-item s-pagination-next s-pagination-disabled'):
        new_page = soup.find('a', class_ = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator').get('href')
        url = 'https://www.amazon.com.br' + new_page
        return url
    else:
        return

def getTitle(result):
    title = result.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').text
    return title

def getPrice(result):
    try:
        price = result.find('span', class_ = 'a-price').find('span', class_ = 'a-offscreen').text
        return price
    except:
        return ''

def getLink(result):
    try:
        href = result.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').parent['href']
        link = 'https://www.amazon.com.br' + href
        return link
    except:
        return ''

def getRating(result):
    try:
        rating = result.find('i', class_ = 'a-icon-star-small')
        rating_count = int(rating.find_parents('span', limit=2)[1].next_sibling.a.span.text)
        return [ rating.text, rating_count ]
    except:
        return ['sem avaliações', 0]

records = []

while url:
    soup = getData(url)
    results = soup.find_all('div', class_ = 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
    
    for result in results:
        
        price = getPrice(result)

        # se NO_PRICE == 0 e não tiver preço no resultado, pula pra próxima iteração
        if not(NO_PRICE or price):
            continue
        
        title = getTitle(result)
        rating, rating_count = getRating(result)
        
        link = getLink(result)
      
        records.append( (title, price, rating, rating_count, link) )
    
    url = getNextPage(soup)

### Salvar infos no Excel
wb = Workbook()
ws = wb.active
ws.append(['Descrição',  'Preço', 'Classificação', 'Num. avaliações', 'Link'])
for record in records:
    ws.append(record)
wb.save('Resultados.xlsx')

print('Pesquisa finalizada!')