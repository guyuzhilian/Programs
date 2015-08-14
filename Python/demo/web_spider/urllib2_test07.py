# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:49

import urllib2
req = urllib2.Request("http://bbs.csdn.net/callmewhy")

try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print(e.code)