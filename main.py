from parse_events import parse_on_going_events, parse_upcoming_events
from fastapi import FastAPI
from headers import headers
import requests
app = FastAPI()


@app.get("/")
async def root():
    return parse_upcoming_events()
