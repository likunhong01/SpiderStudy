#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/20 14:54'
__author__ = 'likunkun'

from selenium import webdriver
class Douyu:
    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li')
        print(li_list)
        content_list = []
        for li in li_list:
            item = {}
            item['img'] = li.find_element_by_xpath('.//img').get_attribute('src')
            print(item['img'])
            item['title'] = li.find_element_by_xpath('.//h3[@class="DyListCover-intro"]').text
            print(item['title'])
            item['zhuboname'] = li.find_element_by_xpath('./div/a[1]/div[2]/div[2]/h2').text
            print(item['zhuboname'])
            item['kind'] = li.find_element_by_xpath('.//span[@class="DyListCover-zone"]').text
            print(item['kind'])
            item['num'] = li.find_element_by_xpath('./div/a[1]/div[2]/div[2]/span').text
            print(item['num'])
            print(item)
            content_list.append(item)
        # 获取下一页
        next_url = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]/span')
        next_url = next_url[0] if len(next_url) > 0 else None

        return content_list, next_url

    def sava(self, content_list):
        pass

    def run(self):
        # start_url
        # 发送请求，获取响应
        self.driver.get(self.start_url)
        # 提取数据，提取下一页
        content_list, next_url = self.get_content_list()
        # 保存数据
        self.sava(content_list)
        # 点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            content_list, next_url = self.get_content_list()
            self.sava(content_list)


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()