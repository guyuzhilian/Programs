# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-06-13 14:36

import urllib2
import urllib
import re
import thread
import time

pattern = re.compile(r'<div.*?class="content">(.*?)<!--(.*?)-->(.*?)</div>', re.S)

class SpiderModel(object):

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def get_page(self, page):
        my_url = "http://www.qiushibaike.com/hot/page/" + page
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        req = urllib2.Request(my_url, headers = headers)
        my_response = urllib2.urlopen(req)
        my_page = my_response.read()
        # unicode_page = my_page.encode("utf-8")

        my_items = pattern.findall(my_page)
        items = []
        for item in my_items:
            items.append([item[0].replace("\n", ""), item[1].replace("\n", "")])
        return items

    def load_page(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    my_page = self.get_page(str(self.page))
                    self.page += 1
                    self.pages.append(my_page)
                except:
                    print("无法链接糗事百科！")
            else:
                time.sleep(1)

    def show_page(self, now_page, page):
        for items in now_page:
            print u"第%d页" % page, items[0], items[1]
            my_input = raw_input()
            if my_input == "quit":
                self.enable = False
                break

    def start(self):
        self.enable = True
        page = self.page

        print(u"正在加载中请稍后......")

        thread.start_new_thread(self.load_page, ())

        while self.enable:
            if self.pages:
                now_page = self.pages[0]
                del self.pages[0]
                self.show_page(now_page, page)
                page += 1

print(u"""
---------------------------------------
    程序：糗百爬虫
    版本：0.3
    作者：why
    日期：2015-06-13
    语言：Python 2.7
    操作：输入quit退出阅读糗事百科
    功能：按下回车依次浏览今日的糗事热点
----------------------------------------
""")

print(u"请按下回车浏览今日的糗百内容：")
raw_input(" ")
my_model = SpiderModel()
my_model.start()