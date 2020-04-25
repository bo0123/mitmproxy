#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 19:57
# @Author  : Aries
# @Site    : 
# @File    : decode_data.py
# @Software: PyCharm

import json
from handle_docker.handle_mongo import mongo_info


def response(flow):
    #抖音
    if 'aweme.snssdk.com/aweme/v1/feed' in flow.request.url:
        douyin_data_dict = json.loads(flow.response.text)
        for douyin_item in douyin_data_dict['aweme_list']:
            mongo_info.insert_item(douyin_item)

    #快手
    elif 'api.gifshow.com/rest/n/feed/hot' in  flow.request.url:
        kuaishou_data_dict = json.loads(flow.response.text)
        for kuaishou_item in kuaishou_data_dict['feeds']:
            mongo_info.insert_item(kuaishou_item)

    #今日头条
    elif 'is.snssdk.com/api/news/feed' in flow.request.url:
        jrtt_data_dict = json.loads(flow.response.text)
        for kuaishou_item in jrtt_data_dict['feeds']:
            mongo_info.insert_item(kuaishou_item)
