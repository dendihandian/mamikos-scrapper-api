from fastapi import FastAPI
from app.routers import area, kost

app = FastAPI()

@app.get("/")
def welcome():
    return {
        "message": "Welcome to Mamikos Scrapper API"
    }

app.include_router(area.router)
app.include_router(kost.router)