from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "hello world"}

@app.get('/greet')
async def greetings(name: Optional[str]="User", age: int=0) -> dict:
    return {"message": f"hello {name}", "age": age}


class CreateBookModel(BaseModel):
    title: str
    author: str

@app.post('/create_book')
async def book_create(book_data: CreateBookModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }