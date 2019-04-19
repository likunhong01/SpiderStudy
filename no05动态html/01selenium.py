#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/19 14:14'
__author__ = 'likunkun'

from selenium import webdriver

# 实例化一个浏览器
driver = webdriver.Chrome()

# 发送请求
driver.get(url='http://www.baidu.com')

# 元素定位方法
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()

# 退出浏览器
import time
time.sleep(5)
driver.quit()

'''-----------------------------'''
#
# # 实例化浏览器
# driver = webdriver.PhantomJS()
#
# # 设置窗口大小
# # driver.set_window_size(1920, 1080)
# # 或者最大化窗口
# driver.maximize_window()
#
# # 页面截屏
# driver.save_screenshot("./baidu.png")
#
# # 获取cookie
# cookies = driver.get_cookies()
# # 结果是[{},{}]，把他转化为字典
# cookies = {i['name']:i['value'] for i in cookies}
#
# # 获取html字符串
# htmp_str = driver.page_source   # 浏览器中的elements内容
#
# # 获取当前url
# url = driver.current_url
#
# # 关闭页面
# driver.close()

# # 退出浏览器
# import time
# time.sleep(3)
# driver.quit()