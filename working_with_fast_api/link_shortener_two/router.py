from fastapi import FastAPI

from url import Url

app = FastAPI()

@app.get("/")
def get_welcome_message():
    return {"message": "Welcome to FastAPI"}

@app.post("/url")
def enter_url(url: str):
    url = Url(url)
    return {"url": url}