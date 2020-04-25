#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 19:35
# @Author  : Aries
# @Site    : 
# @File    : handle_mongo.py.py
# @Software: PyCharm

import pymongo
from pymongo.collection import Collection




client = pymongo.MongoClient(host='192.168.66.100',port=27017)
db = client['douyin']

def handle_init_task():
    task_id_collections = Collection(db, 'task_id')
    with open('douyin_hot_id.txt','r') as f:
        f_read = f.readlines()
        for i in f_read:
            task_info = {}
            task_info['share_id'] = i.replace('\n','')
            task_id_collections.insert(task_info)


def save_task(task):
    task_collections = Collection(db,'task_id')
    task_collections.update({'share_id':task['share_id']},task,True)



def handle_insert_douyin(douyin_info):
    task_id_collections = Collection(db, 'douyin_info')
    task_id_collections.insert(douyin_info)


def handle_get_task():
    task_id_collections = Collection(db, 'task_id')
    # return task_id_collections.find_one({})
    return task_id_collections.find_one_and_delete({})

handle_init_task()
