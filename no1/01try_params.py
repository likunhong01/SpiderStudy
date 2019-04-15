#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/12 19:14'
__author__ = 'likunkun'

import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"}

p = {"wd":'lkh'}
url_tmp = 'https://www.baidu.com/s?'
# url_tmp = 'https://www.baidu.com/s'

r = requests.get(url_tmp,headers=headers,params=p)
print(r.status_code)
print(r.request.url)

url = 'https://www.baidu.com/s?wd={}'.format("lkh")
r = requests.get(url,headers=headers)
print(r.status_code)
print(r.request.url)