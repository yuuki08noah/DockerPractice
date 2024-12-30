import pymysql.cursors
from fastapi import FastAPI
import pymysql
from pydantic import BaseModel
import os

class Document(BaseModel):
    title: str
    content: str

app = FastAPI()
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

@app.get("/documents")
async def documents():
    connection = pymysql.connect(host='database', port=3306, user='root', password=MYSQL_ROOT_PASSWORD, db=MYSQL_DATABASE, charset='utf8mb4')
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    SQL = f'select * from documents'
    cursor.execute(SQL)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return data

@app.post("/documents")
async def post(document: Document):
    connection = pymysql.connect(host='database', port=3306, user='root', password=MYSQL_ROOT_PASSWORD, db=MYSQL_DATABASE, charset='utf8mb4')
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    SQL = f"insert into documents(title, content, createdAt) values('{document.title}', '{document.content}', now())"
    cursor.execute(SQL)
    connection.commit()
    cursor.close()
    connection.close()