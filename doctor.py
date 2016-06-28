# coding=utf-8
import urllib
import urllib2
import re


class Doctor(object):

    """docstring for Doctor"""

    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
        self.headers = {'User-Agent': 'self.user_agent'}

    # 获取医院页面代码
    def getHospital(self, url):
        req = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(req)
        return response.read().decode('utf-8')

    def getKeshi(self):
        page = self.getHospital(url)
        pattern = re.compile('<a class="ishao" href=".*?" onmousedown.*?</a>', re.S)
        items = re.findall(pattern, page)
        print items
        
        contents = []
        print 222
        for item in items:
            print items
            contents.append(item)
        return contents
        
        


url = 'http://www.guahao.com/hospital/b20f1915-66d5-46d9-b539-0d742b0eedd6000'
test = Doctor()
test.getKeshi()
