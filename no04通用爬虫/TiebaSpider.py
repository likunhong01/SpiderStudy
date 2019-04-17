import requests
import json
import re
from lxml import etree
 
class TiebaSpider:
	def __init__(self,tieba_name):
		self.tieba_name = tieba_name
		self.start_url = '' + tieba_name + ''
		self.headers = ''

	def parse_url(self, url):
		response = requests.get(url,headers=self.headers)
		return response.content.decode()
		
	def get_content_list(self, html_str):	# 提取数据
		html = etree.HTML(html_str)
		div_list = html.xpath('//div[contains(@class,"i")]')	# 根据div分组
		content_list = []
		for div in div_list:
			item = {}
			item['title'] = div.xpath('./a/text()')[0] if len(div.xpath('./a/text()')) > 0 else None
			item['href'] = div.xpath('./a/@href')[0] if len(div.xpath('./a/@href')) > 0 else None
			item['img_list'] = self.get_img_list(item['href'])
			content_list.append(item)
		# 提取下一页url地址
		next_url = html.xpath('//a[text()="下一页"')
		return content_list,next_url

	def get_img_list(self, detail_url):	# 获取帖子中的所有图片
		# 3.2-3.4
		return img_list
		pass

	def sava_content_list(self,content_list):	# 保存数据
		file_path = self.tieba_name + '.txt'
		with open(file_path, 'a',encoding='utf-8') as f:
			for content in content_list:
				f.write(json.dumps(content, ensure_ascii=False, indent=2))
				f.write('\n')

	def run(self):
		next_url = self.start_url
		while next_url is not None:
			# 1.start_url
			# 2.发送请求，获取响应
			html_str = self.parse_url(next_url)
			# 3.提取数据，提取下一页的url地址
			# 3.1提取列表页的url地址和标题
			# 3.2提取列表页的url地址，获取详情页的第一页
			# 3.3提取详情页第一页的图片，提取下一页的地址
			# 3.4请求详情页下一页的地址，进入循环3.2-3.4
			content_list,next_url = self.get_content_list(html_str)
			# 4.保存数据
			self.sava_content_list(content_list)
			# 5.请求下一页的url地址，进入循环2-5
