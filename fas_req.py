import requests
from lxml import etree


test_url = 'https://webhook.site/3bf819a3-accf-4f1f-9c0a-aee6d724f3e9?'

url = 'http://apps.eias.fas.gov.ru/FindCEM/Search/Report'
session = requests.session()


"""Получаем cookie"""
cookies_url = 'http://apps.eias.fas.gov.ru/FindCem/'

get_cookies = session.get(url=cookies_url)
cookie = get_cookies.cookies
print(f'Cookie: {cookie}')


"""Получаем токен формы"""
htmlparser = etree.HTMLParser()
tree = etree.parse(cookies_url, htmlparser)

token = tree.xpath('//input[@name="__RequestVerificationToken"]/@value')[0]
print(f'Token: {token}')



payload = {
    '__RequestVerificationToken': token
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'apps.eias.fas.gov.ru',
    'Origin': 'http://apps.eias.fas.gov.ru',
    'Referer': 'http://apps.eias.fas.gov.ru/FindCem/',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}




# resp = session.post(url=url, data=payload, cookies=cookie, headers=headers)
resp = session.post(url=test_url, headers=headers, data=payload, cookies=cookie)
# print(resp.text)


