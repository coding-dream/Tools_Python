#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as Jsoup

# document = Jsoup("<html><div></div></html>")
# document = Jsoup(filename=path) #传入文件
document = Jsoup(url='http://python.jobbole.com/all-posts/page/1/')
# html = document.html()
# html = document.text()

# 网页请求功能
# print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
# print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)

# 选择器
hrefs = document(".archive-title")
# hrefs = document("#archive-title")

for href in hrefs.items():
    text = href.text()
    a_href = href.attr("href")

    print(text + " " + a_href)

print()
print()

document = Jsoup(url="http://www.java1234.com/a/javabook/javaweb/",encoding="utf-8")
lis = document(".listbox")("ul.e2")("li")

document.make_links_absolute(base_url='http://www.java1234.com/')
for li in lis.items():
    name = li("a").text()
    url = li("a").attr("href")
    print(name + " " + url)
