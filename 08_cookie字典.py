#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 16:11'
__author__ = 'likunkun'


import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400",
}
cookie = 'uuid_tt_dd=10_19738602580-1550238847768-288332; smidV2=201806261525175bb6073251aadb0e8ec6780b39a1083500e39a956017c6860; UN=likunkun__; _ga=GA1.2.1498254973.1550715937; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*likunkun__!6525*1*10_19738602580-1550238847768-288332; UM_distinctid=169910065fab7-0127b7fe9353f-335e407d-e1000-169910065fb10f; UserName=likunkun__; UserInfo=768c38fdeb434b57a9885752abd633c5; UserToken=768c38fdeb434b57a9885752abd633c5; UserNick=%E6%98%86%E6%98%86%E6%AC%A7%E7%B2%91%E7%B2%91; AU=3AB; BT=1553177748171; dc_session_id=10_1555216967176.487517; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22def64da06c960f6e860e0412ba65c88a%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22123.139.179.122%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+WOW64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F63.0.3239.26+Safari%2F537.36+Core%2F1.63.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1555229601%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22userInfo%22%3Bs%3A10%3A%22likunkun__%22%3B%7Dc3e3a409a060feefc0ac0f89a7810d80; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1554992965,1554994801,1555069053,1555229602; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1555229602; dc_tos=ppxyua'
cookies = {i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
print(cookies)

# 有cookie就可以直接带着cookie拿登录后的界面
r = requests.get('http://www.renren.com/327550029/profile', headers=headers,cookies=cookies)

# 保存页面
with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
