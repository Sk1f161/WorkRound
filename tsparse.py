#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
import csv

BASE_URL = 'http://www.weblancer.net/projects/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count(html):
    soup = BeautifulSoup(html, "lxml")
    paggination = soup.find('div', class_='pages_list text_box')
    #if paggination == None:
    #    return paggination == 1
    #print(paggination)
    return int(paggination.find_all('a')[-2].text)

def parse(html):
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', class_='items_list')
    #rows = table.find_all('tr')[1:]
    projects = []
    #
    for row in table.find_all('tr')[1:]:
         cols = row.find_all('td')

         projects.append({
             'title' : cols[0].a.text,
             'categories' : [ category.text.strip() for category in cols[0].div.find_all('noindex')],
             'price' : cols[1].text.strip(),
             'application': cols[2].text.strip().split()[0]
         })

    return projects

def main():
    #parse(get_html(BASE_URL))
    page_count = get_page_count(get_html(BASE_URL))
    print('Всего найденно страниц %d' % page_count)

    projects = []

    for page in range(1, page_count):
        print('Парсим  %d%%' % (page / page_count * 100))
        projects.extend(parse(get_html(BASE_URL + '?page=%d' % page)))

    save(projects, 'projects.csv')

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект','Категори','Цена','Заявки'))

        for projects in projects:
            writer.writerow((projects['title'], ','.join(projects['categories']), projects['price'], projects['application']))


if __name__ == '__main__':
    main()
