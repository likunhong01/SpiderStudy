#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/15 19:24'
__author__ = 'likunkun'

import requests
import json

class Douban:
    def __init__(self):
        self.url_temp_list = [
            {
                'url_temp': 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288',
                'name': '影院热映'
            },
            {
                'url_temp': 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_latest/items?start=0&count=18&loc_id=108288',
                'name': '新片速递'
            }
        ]
        self.headers = {
            'Referer':'https://m.douban.com/movie/nowintheater?loc_id=108288',
            'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'
        }

    # 发送请求获取响应
    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 提取数据
    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        # print(dict_ret)
        content_list = dict_ret['subject_collection_items']
        total = dict_ret['total']
        return content_list, total

    # 保存数据
    def sava_content_list(self, content_list, name):
        name = name + '.txt'
        with open(name, 'a', encoding='utf-8') as f:
            for content in content_list:
                # content['name'] = name
                f.write(json.dumps(content,ensure_ascii=False))
                f.write('\n')   # 写入换行符
        print('保存成功')

    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            total = 18
            while num < total + 18:
                # 1.start_url
                url = url_temp['url_temp'].format(num)
                # 2.发送请求获取响应
                json_str = self.parse_url(url)
                # 3.提取数据
                content_list, total = self.get_content_list(json_str)
                # 4.保存
                self.sava_content_list(content_list, url_temp['name'])
                # if len(content_list) < 18:
                #     break
                # 5.构造下一页的url地址，循环
                num += 18

if __name__ == '__main__':
    douban = Douban()
    douban.run()