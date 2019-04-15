#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 17:16'
__author__ = 'likunkun'

import requests

response = requests.get('http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png',)
with open('a.png', 'wb') as f:
    f.write(response.content)
