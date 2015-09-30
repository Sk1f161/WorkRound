# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen

#html_doc = urlopen('https://m.avito.ru/rostovskaya_oblast/avtomobili').read()
html_doc = urlopen('https://www.avito.ru/rostovskaya_oblast/avtomobili').read()
soup = BeautifulSoup(html_doc)

# print soup
# for meta in soup.find_all('meta'):
#     print(meta.get('content'))

# for link in soup.find_all('a'):
#     print link.get('href')

# for link in soup.find_all('a'):
#     print link.contents[0]

#section = soup.find('section', 'b-content-main')
#1#for link in  soup.find_all('article'):
##    print link.a['href']

#article = section.find_all('article')
#print len(article)
#print article[0]

# print soup.find('div', id='top_menu')

# for img in soup.find_all('img'):
#     print img.get('src')


#2#for location in  soup.find_all('span','info-location'):
##    print location.text

#3#for ticketname in  soup.find_all('span','header-text'):
##    print ticketname.text

#4#for price in soup.find_all('div', 'item-price'):
#    print price.text

#1full#for title in soup.find_all('h3','title'):
#    print title.text

for title in soup.find_all('h3','title'):
    print title.text
