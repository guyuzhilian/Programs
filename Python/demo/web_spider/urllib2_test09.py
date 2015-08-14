# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-05-29 17:51

from urllib2 import Request, urlopen, URLError, HTTPError

req = Request("http://bbs.csdn.net/callmewhy")

try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, "code"):
        print("The server couldn't fulfill the request.")
        print("Error code:", e.code)
    elif hasattr(e, "reason"):
        print("We failed to reach a server")
        print("Reason:", e.reason)
else:
    print("No exception was raised.")