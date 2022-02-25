from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime
from sqlalchemy import Integer

engine = create_engine('sqlite:///fas_table3.sqlite3', echo=True)

metadata = MetaData(bind=engine)

fas_table = Table('inn_date', metadata,
                  Column('id', Integer, primary_key=True),
                  # Column('company_name', String),
                  Column('inn', Integer),
                  Column('date_chk', DateTime)
                  )


metadata.create_all(engine)





