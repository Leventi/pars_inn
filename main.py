import re
import pandas as pd
import pangres
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from pangres import upsert


URL = "./fas/saved_resource_part_2.html"
page = open(URL, encoding='utf-8')

inn_dict = {'inn': []}


def get_inn():
    # response = requests.get(URL)
    section = BeautifulSoup(page.read(), "html.parser")
    items_list = section.findAll('nobr', text=re.compile('ИНН'))

    for item in items_list:
        inn_dict['inn'].append((item.get_text())[5:])

    df = pd.DataFrame.from_dict(inn_dict)
    print(df)

    engine = create_engine('sqlite:///fas_table.sqlite3', echo=True)

    df.to_sql(con=engine, name='fas_table', if_exists='append', index_label='id')

    upsert(con=engine, df=df, table_name='fas_table', if_row_exists='update')

    # df.index.name = 'id'
    # pandabase.to_sql(df, table_name='fas_table', con=engine, how='upsert')


get_inn()
