#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/19 15:23'
__author__ = 'likunkun'

from selenium import webdriver
import requests

# 实例化
driver = webdriver.PhantomJS()
driver.get('https://www.douban.com/')

# 填充用户名密码
driver.find_element_by_id('username').send_keys('18679959330')
driver.find_element_by_id('password').send_keys('35278479')

'''这里可能有验证码，如果有验证码就用云打码平台搞定'''
# 获取图片url地址
yzm_url = driver.find_element_by_id('captcha_image').get_attribute('src')
yzm_content =requests.get(yzm_url).content

# 云打码获取
# from yundama.dama import indetify
# yzm_code = indetify(yzm_content)
#
# # 输入验证码
# driver.find_element_by_id('captcha_field').send_keys(yzm_code)


# 点击提交
driver.find_element_by_class_name('btn-account').click()

# 获取cookies
cookies = {i['name']:i['value'] for i in driver.get_cookies()}
print(cookies)

import time
time.sleep(5)
driver.quit()

