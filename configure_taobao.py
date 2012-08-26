# -*- coding: utf-8 -*-
class Configure:
	## 搜索页url
	queryPattern = r'http://s.taobao.com/search?q={queryString}'
	site=r"淘宝"
	## 搜索词的编码
	encoding='utf-8'
	pager="&s={}"
	## 开始页
	pageStart=0
	## 匹配商品页的正则
	itemPagePattern=r'http://item\.taobao\.com/.*'
	imgSrcAlt="data-ks-lazyload"
	pagelimit =2
	pageSize=40
	outputFolder="output"
	templateFolder="templates"
	template="memories"
	imgFormat="JPEG"
	imgSuffix=".jpg"
	imgSize=(210,160)