# -*- coding: utf-8 -*-
from sgmllib import SGMLParser
import re

class ImgParser(SGMLParser):
	lastHref=""
	images=[]
	items=set()
	configure=None

	def reset(self):
		SGMLParser.reset(self)
		self.pieces=[]

	def _appendImage(self,src):
		self.images.append((self.lastHref,src))
		self.items.add(self.lastHref)
		self.lastHref=''

	def unknown_starttag(self, tag, attributes):
		## 算法：对上一个超链接里的内容进行正则匹配，如果符合商品格式，则认为下一张图片为商品图片
		if tag=="a":
			dic=convertToDictionary(attributes)
			if dic.has_key('href'):
				link=dic['href']
				if re.match(self.configure.itemPagePattern,link) and link not in self.items:
					self.lastHref=dic['href']		
				else:
					self.lastHref=''

		elif tag=="img":
			dic=convertToDictionary(attributes)
			if not self.lastHref:
				return
			## 有些延迟加载图片的站点会把src写在其他属性里
			if self.configure.imgSrcAlt:
				if dic.has_key(self.configure.imgSrcAlt):
					self._appendImage(dic[self.configure.imgSrcAlt])
				elif dic.has_key('src'):
					self._appendImage(dic['src'])
			elif dic.has_key('src'):
				self._appendImage(dic['src'])

## TODO:将二元tuple组成的list转换成map,找不到python有没有这个方法，先自己写了..
def convertToDictionary(tuples):
	dic={}
	for t in tuples:
		dic[t[0]]=t[1]
	return dic