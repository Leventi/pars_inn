from requests import Session
from bs4 import BeautifulSoup


def get_token(text):
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


"""Получаем cookie"""
get_cookies = session.get(url=cookies_url, headers=headers)

"""Получаем токен формы"""
token = get_token(get_cookies.text)

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
    'Origin': 'http://apps.eias.fas.gov.ru',
    'Referer': 'http://apps.eias.fas.gov.ru/FindCem/',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

"""Получаем таблицу с данными"""
resp = session.post(url=url, headers=headers, data=payload)
print(resp.text)
