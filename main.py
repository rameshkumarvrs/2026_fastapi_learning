from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "hello world"}

@app.get('/greet')
async def greetings(name:str) -> dict:
    return {"message": f"hello {name}"}