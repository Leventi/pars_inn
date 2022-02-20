from sqlalchemy import create_engine, Column, Integer, log
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from regex_inn import inn_list


engine = create_engine('sqlite:///fas_table2.sqlite3', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class InnFas(Base):
    __tablename__ = 'inn'
    id = Column(Integer, primary_key=True)
    inn = Column(Integer, unique=True)


Base.metadata.create_all(engine)

"""
Проверяем есть ли такой ИНН. Если нет, создаём запись.
"""
def get_or_create(model, **kwargs):
    instance = get_instance(model, **kwargs)
    if instance is None:
        instance = create_instance(model, **kwargs)
    return instance


def create_instance(model, **kwargs):
    try:
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
    except Exception as msg:
        msg_text = 'model:{}, args:{} => msg:{}'
        log.error(msg_text.format(model, kwargs, msg))
        session.rollback()
        raise(msg)
    return instance


def get_instance(model, **kwargs):
    try:
        return session.query(model).filter_by(**kwargs).first()
    except NoResultFound:
        return


for item in inn_list:
    get_or_create(InnFas, inn=item)
    session.commit()



