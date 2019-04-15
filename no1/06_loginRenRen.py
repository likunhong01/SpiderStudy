#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 12:41'
__author__ = 'likunkun'

import requests

session = requests.session()
post_url = 'http://www.renren.com/'
post_data = {"email":"lkk", "password":'lkk'}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
}
# 使用session发送post请求，cookie就会保存在之中
session.post(post_url,data=post_data,headers=headers)
# 再使用session进行请求登录后才能访问的那个地址
r = session.get('http://www.renren.com/327550029/profile',headers=headers)

# 保存页面
with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
