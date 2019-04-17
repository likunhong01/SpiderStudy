from lxml import etree


text = '''
		<div> 
			<ul> 
				<li class="item-1"><a>first item</a></li> 
				<li class="item-1"><a href="link2.html">second item</a></li> 
				<li class="item-inactive"><a href="link3.html">third item</a></li> 
				<li class="item-1"><a href="link4.html">fourth item</a></li> 
				<li class="item-0"><a href="link5.html">fifth item</a>  
			</ul> 
		</div>
'''

html = etree.HTML(text)
print(html)

print("*" * 100)

# 查看element对象中包含的字符串
print(etree.tostring(html).decode())

print("*" * 100)

#获取class为item-1的li下的a的href
ret1 = html.xpath('//li[@class="item-1"]/a/@href')
print(ret1)

print("*" * 100)

# 获取class为item-1 li下的a的文本
ret2 = html.xpath('//li[@class="item-1"]/a/text()')
print(ret2)

print("*" * 100)

# 每个li是一个新闻，把url和文本组成字典
for href in ret1:
	item = {}
	item['href'] = href
	item['title'] = ret2[ret1.index(href)]
	print(item)

print("*" * 100)

# 分组，根据li标签进行分组，对每一组继续写path	
ret3 = html.xpath('//li[@class="item-1"]')
# print(ret3)
for i in ret3:
	item = {}
	item['title'] = i.xpath('./a/text()')[0] if len(i.xpath('./a/text()'))>0 else None
	item['href'] = i.xpath('./a/text()')[0] if len(i.xpath('./a/text()'))>0 else None
	print(item)
