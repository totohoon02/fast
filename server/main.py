import uvicorn
from fastapi import FastAPI
from web import explorer, creature

app = FastAPI()

# router include
app.include_router(explorer.router)
app.include_router(creature.router)


@app.get("/")
def home():
    return "hello"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
