# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:14

import urllib2

response = urllib2.urlopen("http://www.baidu.com")
html = response.read()
print(html)