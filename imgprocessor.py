# -*- coding: utf-8 -*-
import urllib2
from configure import Configure
from PIL import Image
def downloadAndFormat(url,file):
	print "downloading image %s to %s" % (url,file)
	try:
		response=urllib2.urlopen(url,'',5)
		f=open(file,'wb')
		f.write(response.read())
		f.close()
	except:
		print "timeout"
	## todo 因为本地没有编译陈工libjpeg，暂时不进行转码
	#convert(file)

def convert(file):
	print "thumbnail and format image %s" % file
	img=Image.open(file)
	img.thumbnail(Configure.imgSize)
	img.save(file,Configure.imgFormat)
