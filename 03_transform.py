#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/13 23:18'
__author__ = 'likunkun'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400'
}
data = {
    'from':'zh',
    'to':'en',
    'query':'你好，再见',
    # 'transtype':'enter',
    # 'simple_means_flag':'3',
    # 'sign':'54706.276099',
    # 'token':'49c8241694c0e2f661ad3b092f84330e'
}

post_url = 'http://fanyi.baidu.com/v2transapi'

import requests
r = requests.post(post_url,data=data, headers=headers)
print(r.content.decode())
