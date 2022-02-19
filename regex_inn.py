import re
from urllib.request import urlopen
from lxml import etree


URL = "./fas/saved_resource_part.html"
page = open(URL, encoding='utf-8').read()


response = urlopen('file:' + URL)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

requisites = tree.xpath('//nobr/div[contains(text(), "ИНН")]/text()')

# pattern = re.compile(r'(?:ИНН:\s)(\d{10,12})')
pattern = re.compile(r'(^\w+:\s)')
inn_list = [re.sub(pattern, '', item) for item in requisites]

print(inn_list)

#проверить урл ReportUrl = '/FindCEM/Search/Report