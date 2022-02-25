import re
import requests
from bs4 import BeautifulSoup

URL = "./fas/saved_resource_part.html"
page = open(URL, encoding='utf-8')

fas_dict = {}


def get_fas():
    # response = requests.get(URL)
    soup = BeautifulSoup(page.read(), "html.parser")
    header = soup.find('thead')
    header_list = header.find_all('th')

    for elem in header_list:
        title = elem.get_text()
        # print(title)

        fas_dict[title] = []

    # print(fas_dict)


    section = soup.find('tbody')
    # items_list = section.findAll('tr')
    items_list = section.findAll('tr')

    print(items_list)

    # for i in items_list:
    #     print(i.text)


    # print(header_list[0])
    # print(items_list[0])


get_fas()