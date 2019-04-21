#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/21 23:05'
__author__ = 'likunkun'

from pymongo import MongoClient


class TestMonogo:
    # 初始化
    def __init__(self):
        client=MongoClient(host="127.0.0.1",port=27017)
        self.collection=client["test"]["t1"]    #->使用方括号的方式选择数据库和集合

    # 插入单个数据
    def test_insert(self):  #insert接收字典，返回obiectId
        ret=self.collection.insert({"name":"test10010","age":33})
        print(ret)

    # 插入多个数据
    def test_insert_many(self):
        item_list=[{"name":"test1000f}".format(i)}for i in range(10)]
        #insert_many接收一个列表，列表中为所有需要插入的字典
        t = self.collection.insert_many(item_list)
        #t.inserted_ids为所有插入的id
        for i in t.inserted_ids:
            print(i)

    # 查找一个元素
    def try_find_one(self):
        # find_one查找并且返回一个结果，接收一个字典形式的条件
        t = self.collection.find_one({"name":"test10005"})
        print(t)

    # 查找多个元素
    def try_find_many(self):
        # find返回所有满足条件的结果，如果条件为空，则返回数据库的所有
        t = self.collection.find({"name":"test10005"})
        # 结果是一个Cursor游标对象，是一个可迭代对象，可以类似读文件的指针，
        for i in t:
            print(i)
        for i in t: #此时t中没有内容
            print(i)

    # 更新一条数据
    def try_update_one(self):
        # update_one更新一条数据
        self.collection.update_one({"name":"test10005"},{"$set":{"name":"new_test10005"}})

    def try_update_many(self):
        #update_one更新全部数据
        self.collection.update_many({"name":"test10005"},{"$set":{"name":"new_test10005"}})

    # 删除一条数据
    def try_delete_one(self):
        self.collection.delete_one({"name":'test10010'})

    # 删除多条数据
    def try_delete_many(self):
        self.collection.delete_many({'name':'test10010'})