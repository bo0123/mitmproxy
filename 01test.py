#coding:utf-8
from mitmproxy import ctx

def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    # ctx.log.warn(str(flow.request.url))
    # ctx.log.error(str(flow.request.headers))



