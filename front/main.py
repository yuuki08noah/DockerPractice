import requests
from fastapi import FastAPI
from pydantic import BaseModel

class Document(BaseModel):
    title: str
    content: str

app = FastAPI()

@app.get("/documents")
async def documents():
    return requests.get("http://back:8000/documents").json()

@app.post("/documents")
async def post(document: Document):
    requests.post("http://back:8000/documents", json=document.dict())

