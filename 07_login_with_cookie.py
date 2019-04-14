#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 16:00'
__author__ = 'likunkun'

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400",
    "Cookie":"登录后的cookie值",
}
# 有cookie就可以直接带着cookie拿登录后的界面
r = requests.get('http://www.renren.com/327550029/profile', headers=headers)

# 保存页面
with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
