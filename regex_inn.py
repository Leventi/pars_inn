import re
from urllib.request import urlopen
from lxml import etree


URL = "./fas/saved_resource_part_2.html"
page = open(URL, encoding='utf-8').read()


response = urlopen('file:' + URL)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

requisites = tree.xpath('//nobr/div[contains(text(), "ИНН")]/text()')
company_name = tree.xpath('//tr/td[5]/text()')

# pattern = re.compile(r'(?:ИНН:\s)(\d{10,12})')
pattern = re.compile(r'(^\w+:\s)')
inn_list_str = [re.sub(pattern, '', item) for item in requisites]
inn_list = [int(i) for i in inn_list_str]

# print(inn_list)

