#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/16 13:13'
__author__ = 'likunkun'

import re
import requests
import json

url = ''
headers = {}

# 爬取内涵段子（由于内涵被封了，只看思路）
# 1.找到starturl
# 2.发送请求，获取响应
str = requests.get(url,headers).content.decode()

# 3.提取数据：content_list是数据，max_time用于换页
# 用正则或者json提取数据

html_str = ''
# 正则
content_list = re.findall(r'', html_str, re.S)
max_time = re.findall("max_time:'(.*?)',", html_str)[0]

json_str = ''
# json
dict_ret = json.loads(json_str)
data = dict_ret['data']['data']
content_list = [i['group']['content'] for i in data]   # 列表生成式
max_time = dict_ret['data']['max_time']
has_more = dict_ret['data']['has_more']

# 4.保存
with open('a.txt', 'a', encoding='utf-8') as f:
    for content in content_list:
        f.write(json.dumps(content))
        f.write('/n')
    print('complete!')

# 5.构造下一页url
# 6.发送请求获取响应
# 7.提取数据
# 8.保存数据
# 9.循环5-8步骤，其实就是1-4步