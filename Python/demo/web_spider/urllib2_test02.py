# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:16

import urllib2

req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
the_page = response.read()
print(the_page)