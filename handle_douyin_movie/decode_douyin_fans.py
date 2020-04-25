import json
try:
    from douyin.handle_mongo import save_task
except:
    from handle_mongo import save_task


def response(flow):
    #通过fildder的方式获取到请求接口
    if 'aweme/v1/user/follower/list' in flow.request.url:
        #数据的分析获取节点中的followers
        for user in json.loads(flow.response.text)['followers']:
            douyin_info = {}
            #分享的id
            douyin_info['share_id'] = user['uid']
            douyin_info['douyin_id'] = user['short_id']
            douyin_info['nickname'] = user['nickname']
            print(douyin_info)
            save_task(douyin_info)
















