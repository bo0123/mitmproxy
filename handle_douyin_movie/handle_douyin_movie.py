#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 17:39
# @Author  : Aries
# @Site    : 
# @File    : handle_douyin_movie.py.py
# @Software: PyCharm
import json
import os
import time

import requests
import re


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#分享ID
share_id = "89923219116"
share_url = "https://www.douyin.com/share/user/"+share_id


header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}

#dytk 和tac的正则表达式
dytk_search = re.compile(r"dytk: '(.*?)'")
tac_search = re.compile(r"<script>tac=(.*?)</script>")
response = requests.get(url=share_url,headers=header)


#处理获取dytk 和tac
dytk = re.search(dytk_search,response.text).group(1)
tac = re.search(tac_search,response.text).group(1)


#tac封装成为js的格式
tac = "var tac="+tac+";"


# html页面的编写合成 header + tac+ foot
with open("html_head.txt") as f1:
    f1_read = f1.read()

with open("html_foot.txt") as f2:
    f2_read = f2.read().replace("&&&&","89923219116")


with open("test.html","w") as f_w:
    f_w.write(f1_read+"\n"+tac+"\n"+f2_read)


# signature = input("秘钥为：")

chrome_options = Options()
chrome_options.add_argument("--headless")
abspath = os.path.abspath(r"D:\PycharmProjects\mitmproxy\handle_douyin_movie\chromedriver.exe")
# douyin_driver = webdriver.Chrome(executable_path=abspath)
douyin_driver = webdriver.Chrome(executable_path=abspath,chrome_options=chrome_options,)
# douyin_driver.get(".\test.html")
douyin_driver.get("file:///D:\\PycharmProjects\\mitmproxy\\handle_douyin_movie\\test.html")
signature = douyin_driver.title
print(signature)
douyin_driver.quit()

# movie_url = "https://www.douyin.com/aweme/v1/aweme/post/?user_id="+share_id+"&count=21&max_cursor=0&aid=1128&_signature="+signature+"&dytk="+dytk
movie_url = "https://www.douyin.com/web/api/v2/aweme/post/?user_id="+share_id+"&count=21&max_cursor=0&aid=1128&_signature="+signature+"&dytk="+dytk
print(movie_url)
#接口不太稳定，所以要使用while循环一直调用
while True:
    movie_reponse = requests.get(url=movie_url,headers=header)
    if json.loads(movie_reponse.text)["aweme_list"] == []:
        time.sleep(1)
        continue
    else:
        print(movie_reponse.text)
        for item in json.loads(movie_reponse.text)["aweme_list"]:
            video_url = item["video"]["play_addr"]["url_list"][0]
            video_response = requests.get(url=video_url,headers=header)
            with open("douy2in.mp4","wb") as v:
                #不能使用video_response.text，必须使用content才可以把内容写进去
                v.write(video_response.content)
                break