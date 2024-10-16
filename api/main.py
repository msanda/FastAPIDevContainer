from typing import Union

from fastapi import FastAPI

import httpx

app = FastAPI()
url = "http://httpbin.org/uuid"


@app.get("/")
def read_root():
    return {"Hello": "World",
            "Status":"Testing DevContainer"}
    
@app.get("/test_get_request")
def read_root():
    client = httpx.Client()
    response = client.get(url)
    return response.json()