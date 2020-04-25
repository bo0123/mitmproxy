"""
https://fanyi.baidu.com/v2transapi?from=en&to=zh

from=en
to=zh
query=python
simple_means_flag=3
sign=477811.239938
token=f10fcf07b16b9594774b364496eade1c
domain=common
"""
import execjs
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import sys,json


class BaiDuFanYi():
    def __init__(self,query):
        self.baseURL = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            "cookie": "BIDUPSID=2F9CB8976314692C5FF0C1226DF66C1A; PSTM=1575423284; BAIDUID=87C0D8531301AA10B721B8E6035AF613:FG=1; BDUSS=B5Q0RxYlVIMGRhSjhVbXo4LVFlMUMtVWR2cWVwSjJWTkdoTzA3RWs4WHYwWkplRVFBQUFBJCQAAAAAAAAAAAEAAABmU7Uyw%7EfNosG8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO9Ea17vRGteZH; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1584872308,1584919955; yjs_js_security_passport=3c2cbb6c9f062260962317c73b43c95273cd2dda_1584925031_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1584925147; __yjsv5_shitong=1.0_7_50261803ebc3b8fc61443d63811925bcd28f_300_1584925151571_111.174.97.217_d34ae965",
            "referer": "https://fanyi.baidu.com/",
        }

        self.from_data = {"from": "en",
                          "to": "zh",
                          "query": query,
                          "simple_means_flag": "3",
                          "sign": self.get_sign(query),
                          "token": "f10fcf07b16b9594774b364496eade1c",
                          "domain": "common", }

    def get_response(self, url):

        try:
            # url_str = req.Request(url,data=self.from_data, headers=self.header)
            # response = req.urlopen(url_str, timeout=10)
            response = requests.post(url,data=self.from_data, headers=self.header)
        except Exception as e:
            print(sys._getframe().f_code.co_name +"请求失败",e)
        else:
            # return response.read().decode("UTF-8")
            return response.text

    def spyder(self):
        html = self.get_response(self.baseURL)
        dict_info =json.loads(html)
        return dict_info

    def get_sign(self,query):
        try:
            with open("code.js", "r") as f:
                ctx = execjs.compile(f.read())
                # r = ctx.call("e", self.query)
                r = ctx.call("e", query)
        except:
            print(sys._getframe().f_code.co_name + "   ERR")
        else:
            print(r)
            return r


if __name__ == "__main__":
    fanyi = BaiDuFanYi("ming")
    # print(fanyi.spyder())
    print(execjs.get().name)