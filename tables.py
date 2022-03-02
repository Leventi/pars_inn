from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from models import engine

Session = sessionmaker(bind=engine)
sessionsql = Session()
Base = declarative_base()


class InnFas(Base):
    __tablename__ = 'full_fas_table'

    id = Column(Integer, primary_key=True)
    inn = Column(String, unique=True)
    company_name = Column(String)
    registry = Column(String)
    section = Column(String)
    doc_number = Column(String)
    region = Column(String)
    address = Column(String)
    order_number = Column(String)
    order_date = Column(String)
    date_chk = Column(DateTime)


Base.metadata.create_all(engine)

