from fastapi import FastAPI
from app.routers import area, kost, kampus, testimonials, room

app = FastAPI()

app.include_router(area.router, tags=['area'])
app.include_router(kost.router, tags=['kost'])
app.include_router(kampus.router, tags=['kampus'])
app.include_router(testimonials.router, tags=['testimonials'])
app.include_router(room.router, tags=['room'])