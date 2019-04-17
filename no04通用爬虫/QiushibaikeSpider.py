#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/17 19:10'
__author__ = 'likunkun'

import requests
import re
import json
from lxml import etree

class QiuShiBaiKe:
    def __init__(self):
        # 起始地址
        self.start_url = 'https://www.qiushibaike.com/text/page/1/'
        # 根网址
        self.root_url = 'https://www.qiushibaike.com'
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
        }

    # 发送请求，获取响应
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_content(self, html_str):
        # 转化为HTML对象
        html = etree.HTML(html_str)
        # 找到所有的段子的div的父亲标签（包含了所有段子div的div）
        divs = html.xpath('//*[@id="content-left"]/div')
        # 用一个列表保存段子，每个段子有作者和内容（字典）
        duanzis = []
        # 对每个段子循环
        for div in divs:
            duanzi = {}
            # 获取作者
            duanzi['author'] = div.xpath('.//h2/text()')[0].replace('\n', '') if len(div.xpath(
                './/h2/text()')) > 0 else None

            # 获取内容，因为内容放在了不同标签中，需要连起来
            if len(div.xpath('.//div[@class="content"]/span/text()')) > 0:
                strs = div.xpath('.//div[@class="content"]/span/text()')
                content = ''
                for str in strs:
                    content += str
                duanzi['content'] = content.replace('\n', '')
            else:
                duanzi['content'] = None

            # 打印测试
            # print(duanzi['author'] + '说：' + duanzi['content'])
            # 把这个段子放进列表
            duanzis.append(duanzi)

        # 获取下一页url
        next_url = self.root_url + html.xpath('//*[@id="content-left"]/ul/li[8]/a/@href')[0] if len(
            html.xpath('//*[@id="content-left"]/ul/li[8]/a/@href')) > 0 else None
        return next_url, duanzis

    # 保存段子
    def save_duanzi(self,duanzis):
        file_path = '段子.txt'
        with open(file_path, 'a', encoding='utf-8') as f:
            for duanzi in duanzis:
                str = duanzi['author'] + '说：' + duanzi['content']
                f.write(json.dumps(str, ensure_ascii=False, indent=2))  # indent是每次递进的空格
                f.write('\n')

    # 处理逻辑
    def run(self):
        # 下一个要获取的网页地址，第一次是起始地址
        next_url = self.start_url
        while next_url is not None:
            # 发送请求，获取响应
            html_str = self.parse_url(next_url)

            # 提取数据，提取下一页url
            next_url, duanzis = self.get_content(html_str)

            # 保存数据
            self.save_duanzi(duanzis)

if __name__ == '__main__':
    qiu = QiuShiBaiKe()
    qiu.run()







# # 请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
# }
#
# # 要爬取的起始页面
# url = 'https://www.qiushibaike.com/text/page/1/'
# while url is not None:
#     # 请求数据获得响应
#     response = requests.get(url, headers=headers)
#     html_str = response.content.decode()
#
#     # 生成HTML对象
#     html = etree.HTML(html_str)
#
#     # 找到放每个段子的父div
#     divs = html.xpath('//*[@id="content-left"]/div')
#
#     # 对每个div（段子）循环
#     for div in divs:
#         duanzi = {}  # 每个段子装在一个字典里，有作者和内容
#         # 获取作者
#         duanzi['author'] = div.xpath('.//h2/text()')[0].replace('\n', '') if len(
#             div.xpath('.//h2/text()')) > 0 else None
#         # 获取内容，因为内容是放在不同div所以要拼接
#         if len(div.xpath('.//div[@class="content"]/span/text()')) > 0:
#             strs = div.xpath('.//div[@class="content"]/span/text()')
#             content = ''
#             for str in strs:
#                 content += str
#             duanzi['content'] = content.replace('\n', '')
#         else:
#             duanzi['content'] = None
#         # 打印测试
#         print(duanzi['author'] + '说：' + duanzi['content'])
#
#     # 根网页
#     root_url = 'https://www.qiushibaike.com'
#     # 下一页地址
#     url = root_url + html.xpath('//*[@id="content-left"]/ul/li[8]/a/@href')[0] if len(
#         html.xpath('//*[@id="content-left"]/ul/li[8]/a/@href')) > 0 else None
