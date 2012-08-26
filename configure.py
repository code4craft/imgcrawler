# -*- coding: utf-8 -*-
class Configure:
	## 搜索页url
	queryPattern = r'http://search.360buy.com/Search?keyword={queryString}&enc=utf-8'
	site=r"京东"
	## 搜索词的编码
	encoding='utf-8'
	## 分页格式
	pager="&page={}"
	## 开始页
	pageStart=0
	## 分页增量
	pageSize=1
	## 抓取页数
	pagelimit =2
	## 匹配商品页的正则，只有商品页面才下载对应图片
	itemPagePattern=r'http://www\.360buy\.com/product/\d+\.html'
	## 很多图片都不是写在src里，而是动态加载的，这是存图片地址的属性
	imgSrcAlt="data-lazyload"
	outputFolder="output"
	templateFolder="templates"
	## 选择的模版
	template="memories"
	imgFormat="JPEG"
	imgSuffix=".jpg"
	imgSize=(210,160)


	

