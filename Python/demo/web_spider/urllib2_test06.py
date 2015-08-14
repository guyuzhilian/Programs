# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:46

import urllib2

req = urllib2.Request("http://www.baibai.com")

try: urllib2.urlopen(req)
except urllib2.URLError, e:
    print(e.reason)