#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 19:06'
__author__ = 'likunkun'

import requests
from retrying import retry

# cookie字典和对象相互转化
response = requests.get("http://www.baidu.com")
print(response.cookies)
print(requests.utils.dict_from_cookiejar(response.cookies))
print(requests.utils.cookiejar_from_dict({'BDORZ': '27315'}))

# url中文解码和编码
print(requests.utils.unquote('https://fanyi.baidu.com/#zh/en/%E4%BD%A0%E5%A5%BD'))
print(requests.utils.quote('https://fanyi.baidu.com/#zh/en/你好'))


# 多次异常捕获模块retry
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'}

@retry(stop_max_attempt_number=3)   # 可以允许报错3次
def _parse_url(url, method, data, proxies):
    if method == 'POST':
        response = requests.post(url,data=data, headers=headers,proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()

def parse_url(url,method='GET',data=None, proxies={}):
    try:
        htmlstr = _parse_url(url, method, data, proxies)
    except:
        htmlstr = None
    return htmlstr
