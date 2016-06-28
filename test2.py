import re
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

url = 'http://www.heibanke.com/lesson/crawler_ex02/'

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open(url)




user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
headers = {'User-Agent': 'user_agent'}

data = {}
data['csrfmiddlewaretoken'] = 'UwbgpA5aVZGFxB5183IAxwrcP2WyiFGx'
data['username'] = 'aixia'

for i in range(31):
	print i
	data = {}
	data['csrfmiddlewaretoken'] = 'UwbgpA5aVZGFxB5183IAxwrcP2WyiFGx'
	data['username'] = 'aixia'
	data['password'] = i
	data = urllib.urlencode(data).encode('utf-8')
	request = urllib2.Request(url, headers=headers, data=data)
	response = urllib2.urlopen(request)
	soup = BeautifulSoup(response.read())
	tip = soup.h3.string
	print tip


cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open(url,data)
for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value
	