from fastapi import FastAPI
from models import database, fas_table


app = FastAPI()


@app.on_event("startup")
async def startup():
    """ когда приложение запускается устанавливаем соединение с БД """
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """ когда приложение останавливается разрываем соединение с БД """
    await database.disconnect()


@app.get("/inn/")
async def read_inn():
    """ получаем все ИНН для теста """
    query = fas_table.select()
    return await database.fetch_all(query)


@app.get("/inn/{company_inn}")
async def read_inn(company_inn: int):
    """ получаем ИНН по указанному в запросе """
    query = fas_table.select().where(fas_table.c.inn == company_inn)
    return await database.fetch_all(query)




