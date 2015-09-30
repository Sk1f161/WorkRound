#!/usr/bin/env python
import requests
from lxml import html
import sys
import urlparse
import os

URL = 'http://www.maximonline.ru/devushki/stars/_article/ani-lorak/'

directory = URL.split("/")[-2]

response = requests.get(URL)
parsed_body = html.fromstring(response.text)

#images = parsed_body.xpath('//img/@src')

#imghref = parsed_body.xpath('//a[@target="_blank"]/@href')

#imghref = parsed_body.xpath('//a[@rel="article-gallery"]/@href')

imghref = parsed_body.xpath('.//*[@rel="article-gallery"]/@target')

print(imghref)

for img in imghref:
     print(img)

#<div class="article-tags tags">
#titext = parsed_body.xpath('//img/@title')
# questins = parsed_body.xpath('//div[@class="article-library-interview-hit-list__question"]/text()')
#
# answers = parsed_body.xpath('//div[@class="article-library-interview-hit-list__answer"]/text()')
#
# print(answers)
#
# for ans in answers:
#     print(ans)
#
# print(images)
#
# if not images:
#      sys.exit("Found No images")
#
# images = [urlparse.urljoin(response.url, url) for url in images]
# print 'Found %s images' % len(images)
#
#
# # for url in images[0:len(images)]:
# #     print(url)
#
# for url in images[0:(len(images)-1)]:
#        r=requests.get(url)
#        print(url.split('/')[-1])
#        if not os.path.exists(directory):
#            os.makedirs(directory)
#        f=open(directory + '/ '+'%s' % url.split('/')[-1],'w')
#        f.write(r.content)
#        f.close()