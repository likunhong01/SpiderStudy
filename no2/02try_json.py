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

# with open('douban.json', 'r', encoding='utf-8') as f:
# 	ret2 = f.read()
# 	ret3 = json.loads(ret2)
# 	print(ret3)
# 	print(type(ret3))

'''json的load和dump是针对包含json的类文件对象使用的，json的loads和dumps是针对json字符串使用的
具有read()和write()方法的对象就是类文件对象，比如f = open('a.text','r')就是类文件对象'''
# 使用json.load提取类文件对象中的数据
with open('douban.json','r',encoding='utf-8') as f:
	ret4 = json.load(f)
	print(ret4)
	print(type(ret4))

# dump可以把python类型放入文件对象中
with open('douban.json','w',encoding='utf-8') as f:
	json.dump(ret1,f,)
