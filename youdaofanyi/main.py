import execjs
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import sys, json, time, random,hashlib

def make_md5(s):
    s=s.encode("utf-8")
    md5=hashlib.md5(s).hexdigest()
    return md5
# print(make_md5("ming"))
#sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
i="love"
ts = str(int(time.time() * 1000))
salt = ts + str(random.randint(0, 9))
sign=make_md5("fanyideskweb" + i + salt + "Nw(nmmbP%A-r6U3EUn]Aj")
user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
bv=make_md5(user_agent)

data = {
    "i": i,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt,
    "sign": sign,
    "ts": ts,
    "bv": bv,
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
}
headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"OUTFOX_SEARCH_USER_ID=404117417@10.169.0.83; JSESSIONID=aaaamFThNyIUu4WPcHfex; OUTFOX_SEARCH_USER_ID_NCOO=1692031186.8784904; ___rl__test__cookies=1584950604953",
    "Host":"fanyi.youdao.com",
    "Origin":"http://fanyi.youdao.com",
    "Proxy-Connection":"keep-alive",
    "Referer":"http://fanyi.youdao.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
response = requests.post(url, data=data,headers=headers).json()
print(response)
# print(response["translateResult"][0][0]["tgt"])
