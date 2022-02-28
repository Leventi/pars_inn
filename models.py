from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime, Integer
import databases

DATABASE_URL = 'sqlite:///fas_table3.sqlite3'
database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

metadata = MetaData(bind=engine)

fas_table = Table('inn_date', metadata,
                  Column('id', Integer, primary_key=True),
                  # Column('company_name', String),
                  Column('inn', Integer),
                  Column('date_chk', DateTime)
                  )


metadata.create_all(engine)





