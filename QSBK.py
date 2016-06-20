#coding:utf-8
import urllib
import urllib2
import re
import thread
import time

#糗事百科f
class QSBK(object):

	#初始化
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/' \
		   '45.0.2454.101 Safari/537.36'
		#初始化headers
		self.headers = { 'User-Agent':self.user_agent }
		#存放段子的变量
		self.stories = []
		#存放程序是否继续运行的变量
		self.enabled = False

	#传入某一页的索引获得页面代码
	def getPage(self,pageIndex):
		try:
			url='http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			#构建请求request
			request = urllib2.Request(url,headers=self.headers)
			#利用urlopen获取页面代码
			response = urllib2.urlopen(request)
			#将页面转到utf-8编码
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print u'连接糗事百科失败，错误原因' \
					  u'',e.reason
				return None

	#传入某一页代码，返回本页1列表
	def getPageItems(self,pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "页面加载失败..."
			return None
		pattern = re.compile('<h2>(.*?)</h2>.*?<div.*?"content">(.*?)</div>.*?<.*?"number">(.*?)</.*?>',re.S)
		items = re.findall(pattern,pageCode)
		#用来存放每页段子的变量
		pageStories = []
		#遍历正则表达式匹配信息
		for item in items:
			pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
		return pageStories

	#加载并提取页面的内容，加入到列表中
	def loadPage(self):
		#如果当前看的页数少于2页，则加载新一页
		if self.enabled == True:
			if len(self.stories) < 2:
				#获取新一页
				pageStroies=self.getPageItems(self.pageIndex)
				#将新一页的段子放入全局stroies中
				if pageStroies:
					self.stories.append(pageStroies)
					self.pageIndex += 1

	#调用该方法，每次敲一次回车输出一个段子
	def getOneStory(self,pageStories,page):
		#遍历一页的段子
		for story in pageStories:
			#等待用户输入
			input = raw_input()
			#每当输入一次回车，判断一下是否要加载新页面
			self.loadPage()
			#如果输入Q则结束程序
			if input == 'Q':
				self.enabled = False
				return
			print u'第%d页\t发布人：%s\t赞：%s\n%s' %(page,story[0],story[2],story[1])

	#开始方法
	def start(self):
		print u'正在读取，回车查看，Q退出'
		#使变量为True,程序可以运行
		self.enabled = True
		#先加载一页
		self.loadPage()
		#局部变量，控制当前读到了第几页
		nowPage = 0
		while self.enabled:
			if len(self.stories) > 0:
				#从全局stories中获取一页段子
				pageStories = self.stories[0]
				nowPage += 1
				#将全局stories中第一个元素删除，因为已经获取过了
				del self.stories[0]
				#输出该页的段子
				self.getOneStory(pageStories,nowPage)


if __name__ == '__main__':
	test = QSBK()
	test.start()








