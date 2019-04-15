#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 11:49'
__author__ = 'likunkun'

import requests

proxies = {
	"http": "http://116.53.197.172:3719",
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
}
r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.status_code)

