#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/18 23:47'
__author__ = 'likunkun'



import requests
import re
import json
from lxml import etree
from queue import Queue
import threading

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

        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

        self.url_queue.put(self.start_url)

    # 发送请求，获取响应
    def parse_url(self):
        while True:
            url = self.url_queue.get()
            if url is not None:
                response = requests.get(url, headers=self.headers)
                self.html_queue.put(response.content)
            self.url_queue.task_done()

    def get_content(self):
        while True:
            html_str = self.html_queue.get()
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

            self.url_queue.put(next_url)
            self.content_queue.put(duanzis)
            self.html_queue.task_done()
            # return next_url, duanzis

    # 保存段子
    def save_duanzi(self):
        while True:
            duanzis = self.content_queue.get()
            # file_path = '段子.txt'
            # with open(file_path, 'a', encoding='utf-8') as f:
            #     for duanzi in duanzis:
            #         str = duanzi['author'] + '说：' + duanzi['content']
            #         f.write(json.dumps(str, ensure_ascii=False, indent=2))  # indent是每次递进的空格
            #         f.write('\n')
            print('保存成功')

            self.content_queue.task_done()

    # 处理逻辑
    def run(self):

        thread_list = []

        t_prase_url = threading.Thread(target=self.parse_url)
        thread_list.append(t_prase_url)

        t_content = threading.Thread(target=self.get_content)
        thread_list.append(t_content)

        t_sava = threading.Thread(target=self.save_duanzi)
        thread_list.append(t_sava)

        for t in thread_list:
            t.setDaemon(True)   #把子线程设置为守护线程，该线程不重要主线程结束，子线程结束
            t.start()

        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()    #让主线程等待阻塞，等待队列的任务完成之后再完成

if __name__ == '__main__':
    print('有问题，下一页url加载太慢，会提前结束')
    qiu = QiuShiBaiKe()
    qiu.run()