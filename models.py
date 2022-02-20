from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer

engine = create_engine('sqlite:///fas_table.sqlite3', echo=True)

metadata = MetaData(bind=engine)

fas_table = Table('fas_table', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('inn', Integer)
                  )

metadata.create_all(engine)





