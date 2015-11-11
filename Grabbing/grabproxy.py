from grab import Grab, GrabError
from urllib.parse import quote
import re

g = Grab()
#https://www.google.ru/search?num=100&q=free%20proxy%20%2B%22%3A8080%22&gws_rd=ssl
g.go('https://www.google.ru/search?num=100&q=' + quote('free proxy +":8080"') + '&gws_rd=ssl')
rex = re.compile(r'(?:(?:[-a-z0-9]+\.)+)[a-z0-9]+:\d{2,4}')
print (g.css_text('body'))
f = open('proxy_list','w')
for proxy in rex.findall(g.css_text('body')):
    g.setup(proxy=proxy, proxy_type='http', connect_timeout=5, timeout=5)
    try:
        g.go('http://google.com')
    except GrabError:
        print (proxy, 'FAIL')
    else:
        print (proxy, 'OK')
        f.write(proxy + '\n')
