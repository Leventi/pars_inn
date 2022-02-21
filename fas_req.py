import requests

url = 'http://apps.eias.fas.gov.ru/FindCEM/Search/Report'

session = requests.Session()

payload = {
    '__RequestVerificationToken': 'h9VufepmXQUM96CKbK5eZaJyPz3O0946OV_XJgHkOB6cc1j372yjbNBviTaD-vp9zY51rraYJIgkRC9BzmZePP_glx3_NTuC6OE8k6jQYzQ1'
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'apps.eias.fas.gov.ru',
    'Origin': 'http://apps.eias.fas.gov.ru',
    'Referer': 'http://apps.eias.fas.gov.ru/FindCem/',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '196',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Cookie': '__RequestVerificationToken_L0ZpbmRDRU01=h7ABEZbvYo-vzVaUO5BVaBQIWxo0ksT9hmg1kqtVmUG7jPKKT7FSTEj8v0JCQ8KVnCJpWY10icS07PNMrPIuGx0KinVtI4OicL8r-i1YW101; ASP.NET_SessionId=gwn5hwxsqwlp10iqp42xatji; _fas_session=NDBRSUtYREczRDkzN3lhZTZSdENUU05UWERPR0JJQVVjV2dFbkhpaFFmR0xGTkRrRXVsTFlHWUVCVHM1SEp1NjhmK3dFTHJ4Vno3Z0VrbHluRkRrQ25GZDUyTXVNTU5FT3YxeGNRbEpJaFFuRW9Ma3o4djI0Y0xDaDFVSEovSk1tWTdtZVc4ZWs5bnVZU0hpN2VlcEZKVk43MHFZWThpRkpHR2tYbmtacDlQcVI5MzBOcGd4MU5XUkxTd0x2VHVxLS1TU3ZmZlluRXFPYlRxbWg4NDZ1anJRPT0%3D--9c3e6ee84db96587e82a5563a0d3a9e1e5263625',
}


resp = session.post(url=url, headers=headers, data=payload)
print(resp.text)


