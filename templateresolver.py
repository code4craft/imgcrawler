# -*- coding: utf-8 -*-
## 根据模版进行内容填充
from configure import Configure
def formatItem(link,img):
	templatePath=Configure.templateFolder+"/"+Configure.template+"/"
	template=open(templatePath+"items.inc","r").read()
	template=template.replace('<!img>',img).replace('<!link>',link)
	return template

def formatIndex(title,content):
	templatePath=Configure.templateFolder+"/"+Configure.template+"/"
	template=open(templatePath+"index.html","r").read()
	template=template.replace('<!title>',title).replace('<!content>',content)
	return template

