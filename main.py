from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/oracle/query")
async def query():
    return {"hi":"hi2"}
