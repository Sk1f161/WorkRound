from grab import Grab
import re

g = Grab()
url='https://www.litmir.co'
g.go("https://www.litmir.co/all_genre")

x={'links':[],'genre':[]}
global_links = g.doc.select("//*[@class='lts9']/a")

for page in global_links:
    #print (page.text())
    x['genre'].append(page.text())
    page_link = page.attr('href')
    x['links'].append(url + page_link)
    #print(page_link)
#    page_link = page.attr('href')
#    post_grab = Grab()
#    post_grab.go(page_link)
#    print(post_grab)

#    try:
#        post_title = post_grab.doc.select("//span[@class='post_title']")[0].text()
#        print(post_title)
#    except IndexError as e:
#        post_title = 'No Title'

global_links = g.doc.select("//*[@class='lt29']")
#print (global_links[0].text())
for page in global_links:
    #print(page.text())
    page_link = page.attr('href')
    #print(page_link)
    x['genre'].append(page.text())
    x['links'].append(url + page_link)

#print(x['genre'][0] + ' : ' + x['links'][0] )
for page in x['genre']:
    print(page)
