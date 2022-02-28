import re
from urllib.request import urlopen
from lxml import etree


URL = "./fas/saved_resource_part.html"
page = open(URL, encoding='utf-8').read()


response = urlopen('file:' + URL)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

pattern = re.compile(r'(^\w+:\s)')

inn_raw = tree.xpath('//nobr/div[contains(text(), "ИНН")]/text()')
inn_list_str = [re.sub(pattern, '', item) for item in inn_raw]
inn_list = [int(i) for i in inn_list_str]

kpp_raw = tree.xpath('//nobr/div[contains(text(), "КПП")]/text()')
kpp_list_str = [re.sub(pattern, '', item) for item in inn_raw]
kpp_list = [int(i) for i in inn_list_str]

ogrn_raw = tree.xpath('//nobr/div[contains(text(), "ОГРН")]/text()')
ogrn_list_str = [re.sub(pattern, '', item) for item in inn_raw]
ogrn_list = [int(i) for i in inn_list_str]


company_name = tree.xpath('//tr/td[5]/text()')
registry = tree.xpath('//tr/td[1]/text()')
section = tree.xpath('//tr/td[2]/text()')
doc_number = tree.xpath('//tr/td[3]/text()')
region = tree.xpath('//tr/td[4]/text()')
adress = tree.xpath('//tr/td[7]/text()')
order_number = tree.xpath('//tr/td[8]/text()')
order_date = tree.xpath('//tr/td[9]/text()')


full_fas_dict = {
    'inn': inn_list,
    'kpp': kpp_list,
    'ogrn': ogrn_list,
    'company_name': company_name,
    'registry': registry,
    'section': section,
    'doc_number': doc_number,
    'region': region,
    'adress': adress,
    'order_number': order_number,
    'order_date': order_date
}








