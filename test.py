import urllib2

url = 'http://jandan.net/ooxx'
req = urllib2.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4')
response = urllib2.urlopen(req)
html = response.read().decode('utf-8')

a = html.find('current-comment-page')
print a
