#coding=utf-8

import re
import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)

try:
	request = urllib2.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0')
	response = urllib2.urlopen(request)

except urllib2.URLError, e:
	if hasattr(e, 'code'):
	    print e.code
	if hasattr(e, 'reason'):
		print e.reason


content = response.read().decode('utf-8')
"""
.*?匹配任意无限多个字符，加上?表示非贪婪
(.*?)表示分组，这个正则分了三组：作者，内容，被赞的次数
re.S 将. 变成任意匹配模式，也可以匹配换行
"""
pattern = re.compile('<h2>(.*?)</h2>.*?<div.*?"content">(.*?)</div>.*?<.*?"number">(.*?)</.*?>',re.S)

items = re.findall(pattern, content)
for item in items:
	print item[0], item[1], item[2] 










#with open('qiushibaike.html', 'w') as f:
#	f.write(content.encode('utf-8'))