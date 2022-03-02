from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime, Integer
import databases

DATABASE_URL = 'sqlite:///fas_table5.sqlite3'
database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

metadata = MetaData(bind=engine)

fas_table = Table('full_fas_table', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('inn', String),
                  Column('kpp', String),
                  Column('ogrn', String),
                  Column('company_name', String),
                  Column('registry', String),
                  Column('section', String),
                  Column('doc_number', String),
                  Column('region', String),
                  Column('address', String),
                  Column('order_number', String),
                  Column('order_date', String),
                  Column('date_chk', DateTime)
                  )


metadata.create_all(engine)





