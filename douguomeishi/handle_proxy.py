import requests

#114.246.2.155"
url = 'http://ip.hahado.cn/ip'
#阿布云
proxy = {'http':'http://H250CBVT21ZIJ74D:79A392F20B6202F0@http-dyn.abuyun.com:9020'}
proxy = {'http':'http://122.231.28.254:15861'}  #快代理
proxy = {'http':'http://27.22.92.150:20824'}  #快代理

# http://dps.kdlapi.com/api/getdps/?orderid=928638770303210&num=2&pt=1&format=json&sep=1
try:
    response = requests.get(url=url,proxies=proxy,timeout=0.5)
    if response.status_code == 200:
        print(response.text)
        print("代理ip没问题")
except Exception as e:
    print("代理ip已失效")
    print(e)
# response = requests.get(url=url)
