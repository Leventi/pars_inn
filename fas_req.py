from requests import Session
from bs4 import BeautifulSoup
import re
from lxml import etree
from tables import sessionsql, InnFas


def get_token_monopoly(text):
    soup = BeautifulSoup(text, 'html.parser')
    el = soup.find("input", {"name": "__RequestVerificationToken"})
    return el['value']


cookies_url = 'http://apps.eias.fas.gov.ru/FindCem/'
url = 'http://apps.eias.fas.gov.ru/FindCEM/Search/Report'

session = Session()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'apps.eias.fas.gov.ru',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}


#получаем cookie сайта
get_cookies = session.get(url=cookies_url, headers=headers)

#получаем токен формы с сайта apps.eias.fas.gov.ru
token = get_token_monopoly(get_cookies.text)


payload = {
    '__RequestVerificationToken': token,
    'RegTypeID': 0,
    'RegPartID': 0,
    'RegionID': 0,
    'OrgName': '',
    'INN': '',
    'OKPO': '',
    'OGRN': '',
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Host': 'apps.eias.fas.gov.ru',
    # 'Origin': 'http://apps.eias.fas.gov.ru',
    'Referer': 'http://apps.eias.fas.gov.ru/FindCem/',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

"""
получаем таблицу с данными: 
ИНН, Наименование компании, Реестр, Раздел, Номер, Регион, Адрес, Номер и дата приказа о включении
"""
resp = session.post(url=url, headers=headers, data=payload)





# Разбор ответа
htmlparser = etree.HTMLParser()
tree = etree.fromstring(resp.text, htmlparser)

all_data_list = tree.xpath('//tbody/tr')

for item in all_data_list:
    try:
        company_name = item.xpath('.//td[5]/text()')[0]
        registry = item.xpath('.//td[1]/text()')[0]
        section = item.xpath('.//td[2]/text()')[0]
        doc_number = item.xpath('.//td[3]/text()')[0]
        region = item.xpath('.//td[4]/text()')[0]
        address = item.xpath('.//td[7]/text()')[0]
        order_number = item.xpath('.//td[8]/text()')[0]
        order_date = item.xpath('.//td[9]/text()')[0]

        inn_raw = item.xpath('.//td[6]/nobr/div[contains(text(), "ИНН")]/text()')

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

    except ValueError:
        print(f"Проблема при разборе и записи входящих данных")

