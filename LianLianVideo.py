#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'limitless'

"""
    blog : http://www.jianshu.com/u/79a88a044955
    use:
    1. python LianLianVideo.py
    2. 输入url类别(如分类地址  http://v.23c.im/rs 填写 rs)
    3. 输入url名称(如视频地址 http://v.23c.im/rs148 填写 rs148)
"""
import requests, json, time, sys


def download(url):
    headers = {'Cookie': 'xa=fe098dade8944d5913de85cef53b52a1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
               'Referer': 'http://m.syasn.com/x2.swf'}
    dest = "F:/" + name + ".mp4"

    requests.adapters.DEFAULT_RETRIES = 5
    response = requests.get(url, headers=headers, stream=True)
    status = response.status_code
    if status == 200:
        total_size = int(response.headers['Content-Length'])
        with open(dest, 'wb') as of:
            for chunk in response.iter_content(chunk_size=102400):
                if chunk:
                    of.write(chunk)
        print("视频：" + name + "已保存到 " + "F盘")
    else:
        print("下载失败：" + str(status))


def parseFor(name):
    url = "http://h.syasn.com/?n=" + name + "&p=222222222"
    headers = {'Cookie': 'xa=fe098dade8944d5913de85cef53b52a1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
               'Referer': 'http://v.23c.im/' + name}
    response = requests.get(url, headers=headers)
    params = response.content.decode() \
                 .replace("mip", "k1") \
                 .replace("mik", "k3") \
                 .replace("min", "k4") \
                 .replace("mis", "k6") \
                 .replace("mid", "k7") \
                 .replace("\'", "") \
                 .replace(",", "&") \
                 .replace(";", "") + "&k2=csgak5sg4m&k5=" + name

    videoUrl = baseVideoUrl + name + "?" + params
    print("正在下载 ->  " + videoUrl)
    download(videoUrl)


if __name__ == "__main__":
    flag = True
    while flag:
        print("\n=========== 下载选项(quit退出) ===========")
        category = input("\n视频类别是：")  # 如分类地址  http://v.23c.im/rs 填写 rs
        name = input("\n视频名称是：")  # 如视频地址 http://v.23c.im/rs148 填写 rs148

        baseVideoUrl = "http://k.syasn.com/" + category + "/"

        if category == 'quit' or name == 'quit':
            flag = False
        else:
            parseFor(name)
