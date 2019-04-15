#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/15 18:33'
__author__ = 'likunkun'

import re
from no2.parse_url import parse_url

url = 'https://36kr.com/'
html_str = parse_url(url)

ret = re.findall('')