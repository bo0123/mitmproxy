#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0:53
# @Author  :  liming
# @Site    : 
# @File    : handle_mongodb.py
# @url    : idig8.com
# @Software: PyCharm

import pymongo
from pymongo.collection import Collection

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="192.168.66.100",port=27017)
        self.db_data = self.client["mongodb"]

    def insert_item(self,item):
        db_collection = Collection(self.db_data,'mongodb')
        db_collection.insert(item)

mongo_info = Connect_mongo()