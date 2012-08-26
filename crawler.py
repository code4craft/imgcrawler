# -*- coding: utf-8 -*-
import sys
import urllib2
import imgprocessor
from sgmllib import SGMLParser
from configure_2012 import Configure
from imgparser import ImgParser
import templateresolver

## 爬虫,按照搜索page进行简单迭代
def crawl(queryWord):
	queryString=urllib2.quote(queryWord,Configure.encoding)
	url=Configure.queryPattern.format(**dict(queryString=queryString))
	pager=Configure.pager
	pages=[]
	newContent=""
	index=0
	items=set()
	for i in range(Configure.pageStart,Configure.pagelimit):
		print "downloading "+url+pager.format(i*Configure.pageSize)
		f=urllib2.urlopen(url+pager.format(i*Configure.pageSize))
		content=f.read()
		f.close()
		images=get_images(content,items)
		for image in images:
			filePath=Configure.outputFolder+"/files/"+str(index)+Configure.imgSuffix
			imgSrc="./files/"+str(index)+Configure.imgSuffix
			link=image[0]
			imgprocessor.downloadAndFormat(image[1],filePath)
			##todo 处理图片
			newContent+=templateresolver.formatItem(link,imgSrc)
			index+=1
	indexFile=open(Configure.outputFolder+'/index.html','w')
	indexFile.write(templateresolver.formatIndex(Configure.site+"搜索："+queryWord,newContent))
	indexFile.close

def get_images(content,items):
	parser = ImgParser()
	parser.configure=Configure
	parser.items=items
	parser.feed(content)
	items=parser.items
	return parser.images

if __name__ == '__main__':
	print u"请选择搜索站点:\n1:京东\n2:淘宝"
	line = sys.stdin.readline()
	if (line.strip()=="2"):
		from configure_taobao import Configure
	print "欢迎使用{}图片墙，请输入搜索关键词".format(Configure.site)
	line = sys.stdin.readline()
	while not line:
		print "关键词不能为空！"
		line = sys.stdin.readline()
	crawl(line)
	print "		-----------------------------------------------------"
	print "		-----------------------------------------------------"
	print "		| all done, please check the file output/index.html |"
	print "		-----------------------------------------------------"
	print "		-----------------------------------------------------"
