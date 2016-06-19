#coding=utf-8
import urllib2
import urllib

url = 'http://www.whatismyip.com.tw'

# 参数是一个字典{'类型': '代理IP: 端口号'}
proxy_support = urllib2.ProxyHandler({'socks': 'teteol.top:779'})

# 定制、创建一个opener
opener = urllib2.build_opener(proxy_support)

# 安装opener
urllib2.install_opener(opener)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)

html = response.read().decode('utf-8')

print type(html)
print html

# 调用opener
#opener.open(url)
