#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/13 23:43'
__author__ = 'likunkun'
import json
import sys

query_string = sys.argv[1]  # 实现在命令行（终端）里翻译

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'
}
data = {
    'from':'zh',
    'to':'en',
    # 'query':'你好，再见',
    'query':query_string,   # 实现在命令行（终端）里翻译
    # 'transtype':'enter',
    # 'simple_means_flag':'3',
    # 'sign':'54706.276099',
    # 'token':'49c8241694c0e2f661ad3b092f84330e'
}

post_url = 'https://fanyi.baidu.com/basetrans'

import requests
r = requests.post(post_url,data=data, headers=headers)
print(r.content.decode())

dict_ret = json.loads(r.content.decode())
ret = dict_ret['trans'][0]['dst']
print('result:',ret)