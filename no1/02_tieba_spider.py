#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/12 19:36'
__author__ = 'likunkun'

import requests
class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=' + tieba_name+ '&ie=utf-8&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400'}

    def get_url_list(self): # 构造url列表，把贴吧的每一页都爬取
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i * 50) for i in range(1000)]

    def parse_url(self, url):   # 发送请求，获取响应
        print(url)
        response = requests.get(url=url,headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):  # 保存html字符串
        file_path = '{}-第{}页.html'.format(self.tieba_name, page_num)
        with open(file_path,'w',encoding='utf-8') as f:  # 黑洞-第1页.html
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # 构造url列表
        url_list = self.get_url_list()
        # 遍历，发送请求，获取相应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存数据
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)

if __name__ == '__main__':
    tieba_spider = TiebaSpider('黑洞')
    tieba_spider.run()