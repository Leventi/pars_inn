from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer

engine = create_engine('sqlite:///fas_table.sqlite3', echo=True)

metadata_obj = MetaData()

fas_table = Table('fas_table', metadata_obj,
                  Column('id', Integer, primary_key=True),
                  Column('inn', Integer)
                  )

metadata_obj.create_all(engine)
