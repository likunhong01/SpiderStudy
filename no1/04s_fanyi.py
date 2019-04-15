#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/4/14 18:31'
__author__ = 'likunkun'
import  requests
import json
import sys
class Baidufanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = 'http://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/basetrans'
        self.headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'}

    def parse_url(self,url, data):  # 发送post请求，获取响应
        response = requests.post(url,data=data, headers=self.headers)
        print(response.content.decode())
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):   # 提取翻译结果
        ret = dict_response['trans'][0]['dst']
        print('result is:',ret)

    def run(self):  # 实现主要逻辑
        # 1.获取语言类型
        # 1.1准备post的url地址，post_data
        lang_detect_data = {'query':self.trans_str}
        # 1.2发送post，获取响应
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)['lan']
        print(lang)
        # 1.3提取语言类型

        # 2.准备post数据
        trans_data = {'query':self.trans_str, 'from':'zh', 'to':'en'} if lang == 'zh' else \
            {'query':self.trans_str, 'from':'en', 'to':'zh'}

        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)

        # 4.提取翻译结果
        self.get_ret(dict_response)

if __name__ == '__main__':
    # trans_str = sys.argv[1]
    baidufanyi = Baidufanyi('你好')
    baidufanyi.run()