import asyncio

import uvicorn
from fastapi import FastAPI, Body, Header

app = FastAPI()


@app.get("/")
async def root():
    return "Hell-o Wrongd!"


@app.get("/hello/{name}")
async def hello_route(name: str):
    return {"message": f"Hello-route {name}"}


@app.get("/hello-query")
async def hello_query(name: str):
    return {"message": f"Hello-query {name}"}


@app.get("/hello-query2")
async def hello_query2(name: str, age: int):
    return {"message": f"Hello {name}, age={age}"}


@app.get("/hello-body")
def hello_body(name: str = Body(embed=True)):
    return f"Hello-body, {name}"

@app.get("/hello-header")
def hello_header(name: str = Header()):
    return f"Hello, {name}"

@app.get("/hello-async")
async def hello_async():
    await asyncio.sleep(5)
    return "Hello as22ync"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
