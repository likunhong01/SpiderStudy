#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/16 12:04'
__author__ = 'likunkun'

b = 'alksdjalksdg1asdgasdg2\nasdgakl'

import re
# 提取\n
a = re.findall('.','\n',re.S)
print(a)
re.findall('.','\n',re.DOTALL)

a = re.findall('a[bcd]e','abe')
print(a)
a = re.findall('a[bcd]+e','abcce')
print(a)
a = re.findall('abce|aede|afce','aede')
print(a)

a = re.findall('<.+>','<asgasadlglsglksal>')
print(a)

b = 'abc123'
a = re.sub('\d','_',b)
print(a)

# 为了节省时间，让每次先编译出来，然后之后每次替换就不需要重新转化
p = re.compile('\d')
a = p.findall(b)
print(a)

a = p.sub('_',b)
print(a)

# 如果有匹配模式，要放到compile里
p = re.compile('.', re.S)
a = p.findall('\n')
print(a)

# r可以消除转义符带来的影响，进行直接的匹配
a = re.findall('a\nb','a\nb')
print(a)

a = re.findall(r'a\nb','a\nb')
print(a)

a = re.findall(r'a\nb','a\\nb')
print(a)

a = re.findall(r'a\\nb','a\\nb')
print(a)

