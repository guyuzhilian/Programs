# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:18

import urllib
import urllib2

url = "http://www.someserver.com/cgi-bin/register.cgi"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {"name": "WHY",
          "location": "SDU",
          "language": "Python" }

headers = {"user-agent": user_agent}
data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()

print(the_page)