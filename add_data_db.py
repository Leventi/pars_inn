# import datetime as dt
# from sqlalchemy import log
# from sqlalchemy.orm.exc import NoResultFound
#
# from tables import sessionsql, InnFas
#
# now = dt.datetime.now(dt.timezone.utc).astimezone()
# time_format = "%Y-%m-%d %H:%M:%S"
#
#
#
#
# # Проверяем есть ли такой ИНН. Если нет, создаём запись.
# def get_or_create(model, **kwargs):
#     instance = get_instance(model, **kwargs)
#     if instance is None:
#         instance = create_instance(model, **kwargs)
#     return instance
#
#
# def create_instance(model, **kwargs):
#     try:
#         instance = model(**kwargs)
#         sessionsql.add(instance)
#         sessionsql.flush()
#
#         with open("log_changes.txt", "a", encoding="utf-8") as file:
#             file.write(f"Добавили новый ИНН {instance.inn} - Дата записи: {now:{time_format}} \n")
#
#     except Exception as msg:
#         msg_text = 'model:{}, args:{} => msg:{}'
#         log.instance_logger(msg_text.format(model, kwargs, msg))
#         sessionsql.rollback()
#         raise(msg)
#     return instance
#
#
# def get_instance(model, **kwargs):
#     try:
#         return sessionsql.query(model).filter_by(**kwargs).first()
#     except NoResultFound:
#         return
#
#
#
# """
# сравниваем таблицы после импорта
# если в базе отсутствует ИНН из списка, пишем в лог ИНН и дату
# """
# def get_inn_list_from_db():
#     db_inn_list = []
#     for i in sessionsql.query(InnFas.inn).all():
#         db_inn_list.append(i[0])
#     print(f"список из базы - {db_inn_list}")
#     print(f"список из файла - {inn_list}")
#
#     diff_list_inn = [i for i in db_inn_list if i not in inn_list]
#
#     for i in db_inn_list:
#         if i not in inn_list:
#             date_to_update = dt.datetime.utcnow()
#
#             #получаем дату по ИНН клиента которого не было в импорте
#             date_mark = sessionsql.query(InnFas).filter(InnFas.inn == i).first()
#
#             #добавляем в лог отсутствующий ИНН с датой
#             if date_mark.date_chk is None:
#                 with open("log_changes.txt", "a", encoding="utf-8") as file:
#                     file.write(f"Данный ИНН отсутствует импорте {i} - Дата проверки: {now:{time_format}} \n")
#
#                 #добавляем дату если ИНН нет в импорте
#                 query = sessionsql.query(InnFas).filter(InnFas.inn == i). \
#                     update({InnFas.date_chk: date_to_update}, synchronize_session=False)
#
#             sessionsql.commit()
#
#     print(f"Разность - {diff_list_inn}")
#
#
#
#
#
#
# #Запускаем итерацию по ИНН из списка
# for item in inn_list:
#     get_or_create(InnFas, inn=item)
#     sessionsql.commit()
#
# #Сравниваем таблицы после импорта
# get_inn_list_from_db()
#
#
#
