# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-06-07 18:44

from urllib2 import Request, urlopen, URLError, HTTPError

old_url = "http://rrurl.cn/b1UZuP"
req = Request(old_url)
response = urlopen(req)
print("Old url :" + old_url)
print("Real url :" + response.geturl())