import datetime
import datetime as dt
from sqlalchemy import create_engine, Column, Integer, log, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from regex_inn import inn_list

engine = create_engine('sqlite:///fas_table3.sqlite3', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

now = dt.datetime.now(dt.timezone.utc).astimezone()
time_format = "%Y-%m-%d %H:%M:%S"


class InnFas(Base):
    __tablename__ = 'inn_date'
    id = Column(Integer, primary_key=True)
    inn = Column(Integer, unique=True)
    date_chk = Column(DateTime)


Base.metadata.create_all(engine)


"""
Сравниваем таблицы после импорта
Если в базе отсутствует ИНН из списка, пишем в лог ИНН и дату
"""
def get_inn_list_from_db():
    db_inn_list = []
    for i in session.query(InnFas.inn).all():
        db_inn_list.append(i[0])
    print(f"Список из базы - {db_inn_list}")
    print(f"Список из файла - {inn_list}")

    diff_list_inn = [i for i in db_inn_list if i not in inn_list]

    for i in db_inn_list:
        if i not in inn_list:
            with open("log_changes.txt", "a", encoding="utf-8") as file:
                file.write(f"Данный ИНН отсутствует импорте {i} - Дата проверки: {now:{time_format}} \n")

            date_to_update = datetime.datetime.utcnow()
            query = session.query(InnFas).filter(InnFas.inn == i). \
                update({InnFas.date_chk: date_to_update}, synchronize_session=False)
            session.commit()

    print(f"Разность - {diff_list_inn}")


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

        with open("log_changes.txt", "a", encoding="utf-8") as file:
            file.write(f"Добавили новый ИНН {instance.inn} - Дата записи: {now:{time_format}} \n")


    except Exception as msg:
        msg_text = 'model:{}, args:{} => msg:{}'
        log.instance_logger(msg_text.format(model, kwargs, msg))
        session.rollback()
        raise(msg)
    return instance


def get_instance(model, **kwargs):
    try:
        return session.query(model).filter_by(**kwargs).first()
    except NoResultFound:
        return




"""Запускаем итерацию по ИНН из списка"""
for item in inn_list:
    get_or_create(InnFas, inn=item)
    session.commit()

"""Сравниваем таблицы после импорта"""
get_inn_list_from_db()



