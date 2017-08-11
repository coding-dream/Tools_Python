#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests, json,time

class UrlManager():
    def getPage(self,url):
        print("currentPage is " + url)
        headers = {'User-Agent': 'Baidu Spidder', 'Referer': 'http://www.baidu.com'}
        response = requests.get(url, headers=headers, verify=False)  # 忽略https
        jsonObject = json.loads(response.content)  # 把json字符串转为python字典
        _list = jsonObject["content"]["data"]["page"]["result"]
        for o in _list:
            self.parse(o)

    def parse(self,o):
        position_id = o["positionId"]  # 职位id
        position_name = o["positionName"]  # 职位名称
        city = o["city"]  # 城市
        create_time = o["createTime"]
        salary = o["salary"]
        company_id = o["companyId"]
        company_name = o["companyName"]
        company_fullName = o["companyFullName"]
        print("\r\n position_id:" + str(position_id) + " position_name:" + position_name + " city:" + city + " salary:" + salary + " company_fullName:" + company_fullName)

        url = "https://m.lagou.com/jobs/"+str(position_id)+".html"

        # not complete

class Demo():
    # 初始各个对象
    def __init__(self):
        pass

    def craw(self):
        pageNo = 1
        url = "https://m.lagou.com/search.json?city=全国&positionName=java&pageNo=" + str(pageNo) + "&pageSize=15"
        urlManager = UrlManager()
        urlManager.getPage(url)

if __name__ == "__main__":
    spider = Demo()
    spider.craw()