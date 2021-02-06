from fastapi import FastAPI
from app.routers import area, kost, kampus

app = FastAPI()

app.include_router(area.router, tags=['area'])
app.include_router(kost.router, tags=['kost'])
app.include_router(kampus.router, tags=['kampus'])