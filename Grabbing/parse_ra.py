import requests
from lxml import html
import sys
import urllib.parse
import os

URL = 'http://autorambler.ru/?utm_content=autorambler&utm_medium=topline&utm_source=news'

directory = URL.split("/")[-2]

response = requests.get(URL)
print(response)
parsed_body = html.fromstring(response.text)

print(parsed_body)

#images = parsed_body.xpath('//img/@src')

#imghref = parsed_body.xpath('//a[@target="_blank"]/@href')

#imghref = parsed_body.xpath('//a[@rel="article-gallery"]/@href')

#posts = parsed_body.xpath('/html/body/div[6]/div[1]/div[1]/div[1]/div[2]/div')

posts = parsed_body.xpath('/*/body/div/div/div/div/div/div/a/@href')
print(posts)

for post in posts:
     print(post)
