# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-06-13 15:24

import urllib2
import re

class HTMLTool(object):
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    EndCharToNoneRex = re.compile("<.*?>")

    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def replace_char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x


class BaiduSpider(object):

    def __init__(self, url):
        self.my_url = url + "?see_lz=1"
        self.datas = []
        self.my_tool = HTMLTool()
        print(u"已经启动百度贴吧爬虫，咔嚓咔嚓")

    def baidu_tieba(self):
        my_page = urllib2.urlopen(self.my_url).read().decode("utf-8")
        end_page = self.page_counter(my_page)
        title = self.find_title(my_page)
        print(u"文章名称：" + title)
        self.save_data(self.my_url, title, end_page)

    def page_counter(self, my_page):
        my_match = re.search(r'class="red">(\d+?)</span>', my_page, re.S)
        if my_match:
            end_page = int(my_match.group(1))
            print(u"爬虫报告：发现楼主共有%d页的原创内容" % end_page)
        else:
            end_page = 0
            print(u"爬虫报告：无法计算楼主发布内容有多少页！")
        return  end_page

    def find_title(self, my_page):
        my_match = re.search(r"<h1.*?>(.*?)</h1>", my_page, re.S)
        title = u"暂无标题"
        if my_match:
            title = my_match.group(1)
        else:
            print(u"爬虫报告：无法加载文章标题！")
        title = title.replace("\\", "").replace("/", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace(">", "")
        return  title

    def save_data(self, url ,title, end_page):
        self.get_data(url, end_page)
        f = open(title + ".txt", "w+")
        f.writelines(self.datas)
        f.close()
        print(u"爬虫报告：文件已下载到本地并打包成txt文件")
        print(u"请按任意键退出...")

    def get_data(self, url, end_page):
        url = url + "&pn="
        for i in range(1, end_page+1):
            print(u"爬虫报告：爬虫%d号正在加载中..." % i)
            my_page = urllib2.urlopen(url + str(i)).read()
            self.deal_data(my_page.decode("utf-8"))

    def deal_data(self, my_page):
        my_items = re.findall('id="post_content.*?>(.*?)</div>', my_page, re.S)
        for item in my_items:
            data = self.my_tool.replace_char(item.replace("\n", "").encode("utf-8"))
            self.datas.append(data + "\n")

print(u"""#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.5
#   作者：why
#   日期：2013-05-16
#   语言：Python 2.7
#   操作：输入网址后自动只看楼主并保存到本地文件
#   功能：将楼主发布的内容打包txt存储到本地。
#---------------------------------------
""")

print(u"请输入贴吧的地址最后的数字串：")
bdurl = "http://tieba.baidu.com/p/" + str(raw_input("http://tieba.baidu.com/p/"))

my_spider = BaiduSpider(bdurl)
my_spider.baidu_tieba()