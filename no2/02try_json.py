import json
import requests
from no2.parse_url import parse_url
from pprint import pprint

# pprint可以美化输出,可以处理字典或者列表数据
url = 'json地址'
html_str = parse_url(url)

# json.loads把json字符串转化为python类型
ret1 = json.loads(html_str)
pprint(ret1)
print(type(ret1))

# json.dumps能够把python类型转化为json字符串，文本类型要用
with open('douban.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(ret1,ensure_ascii=False,indent=2))	# indent表示每级之间空两格，ensreascii表示中文不转化为编码

with open('douban.json', 'r', encoding='utf-8') as f:
	ret2 = f.read()
	ret3 = json.loads(ret2)
	print(ret3)
	print(type(ret3))
