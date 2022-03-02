import re
from urllib.request import urlopen
from lxml import etree
from tables import sessionsql, InnFas
# from add_data_db import get_instance


URL = "./fas/saved_resource_part.html"
page = open(URL, encoding='utf-8').read()


response = urlopen('file:' + URL)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

all_data_list = tree.xpath('//tbody/tr')

try:
    for i in all_data_list:
        company_name = i.xpath('.//td[5]/text()')[0]
        registry = i.xpath('.//td[1]/text()')[0]
        section = i.xpath('.//td[2]/text()')[0]
        doc_number = i.xpath('.//td[3]/text()')[0]
        region = i.xpath('.//td[4]/text()')[0]
        address = i.xpath('.//td[7]/text()')[0]
        order_number = i.xpath('.//td[8]/text()')[0]
        order_date = i.xpath('.//td[9]/text()')[0]

        inn_raw = i.xpath('.//td[6]/nobr/div[contains(text(), "ИНН")]/text()')

        if len(inn_raw) == 0:
            inn_raw = None
        else:
            pattern = re.compile(r'(^\w+:\s)')
            inn_raw = re.sub(pattern, '', inn_raw[0])


        full_fas_dict = {
            'inn': inn_raw,
            # 'kpp': kpp_list,
            # 'ogrn': ogrn_list,
            'company_name': company_name,
            'registry': registry,
            'section': section,
            'doc_number': doc_number,
            'region': region,
            'address': address,
            'order_number': order_number,
            'order_date': order_date
        }

        instance = sessionsql.add(InnFas(**full_fas_dict))
        sessionsql.commit()
except:
    print(f'Проблема при разборе или записи входящих данных')









