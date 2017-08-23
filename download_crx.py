#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests, json,time

baseUrl = "https://ext.chrome.360.cn/provider/extlist/?category=全部&count=100&sortType=download&token=" # 50 页
class UrlManager():
    def getPage(self,page):
        currentPage = baseUrl + str(page)
        print("currentPage is " + currentPage)
        headers = {'User-Agent': 'Baidu Spidder', 'Referer': 'http://www.baidu.com'}
        response = requests.get(currentPage, headers=headers, verify=False)  # 忽略https

        # jstr = '{"name":"xiaoming","age":"22"}'
        # jstr = "{'name':'xiaoming','age':'22'}" // 错误，按照上面的写法

        # jdata = json.dumps(jstr) # 把python字典转为json字符串
        jsonObject = json.loads(response.content.decode("utf-8"))  # 把json字符串转为python字典
        _list = jsonObject["list"]
        for o in _list:
            name = o["name"]
            crxUrl = o["filename"]
            version = o["version"]
            descpic = o["descpic"] # 图片
            self.download(name,crxUrl)
    def download(self,name,url):
        time.sleep(0.2)  # 0.2s
        print("正在下载 == 》 "+ name)
        prefix = name + "_"
        headers = {'User-Agent': 'Baidu Spidder','Referer':'http://www.baidu.com'}
        response = requests.get(url,headers=headers)
        filename = url.split("/")[-1]
        dest = "F:/" + prefix + filename
        try:
            with open(dest,"wb") as fout:
                fout.write(response.content)
        except Exception as e:
            print(dest + " 发生异常")
        print("《===="+name+" 下载完成====》")

class Demo():
    # 初始各个对象
    def __init__(self):
        self.urlManager = UrlManager()

    def craw(self):
        print(" begin")
        for u in range(5,10):
            self.urlManager.getPage(u)

if __name__ == "__main__":
    spider = Demo()
    spider.craw()