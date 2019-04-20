#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/19 23:55'
__author__ = 'likunkun'

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.douyu.com/directory/all')
# x = driver.find_element_by_xpath('//*[@id="listAll"]/section[1]/div[1]/div[1]/h2').text
x = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]//img')
count = 0
for img in x:
    src = img.get_attribute('src')
    count +=1
    print(src)

print(count)