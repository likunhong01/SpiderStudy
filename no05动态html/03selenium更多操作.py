#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/19 19:32'
__author__ = 'likunkun'

from selenium import webdriver
import requests


driver = webdriver.PhantomJS()
driver.get('http://www.')

'''用xpath获取'''
# 获取第一个
ret1 = driver.find_element_by_xpath('//ul[@id="detail-list"]/li')
# 获取全部的符合的：
ret2 = driver.find_elements_by_xpath('//ul[@id="detail-list"]/li')
for li in ret2:
    print(li.find_element_by_xpath('.//a[@class="image share_url"').get_attribute('href'))


'''用link_text'''
# 可以找到内容是下一页的那个标签，还会自动补全url
driver.find_element_by_link_text('下一页>').get_attribute('href')

'''partial_link_text'''
#不完全文本，有包含下一页的都会得到
driver.find_element_by_link_text('下一页').get_attribute('href')

'''tag_name'''
# 标签名，比如div，span等等

'''class_name'''
# 根据样式名称
'''class_selectors'''
# 根据css选择器，w3cschool有使用方法


driver.quit()


