from fastapi import APIRouter
from bs4 import BeautifulSoup
from app.helpers.helper import get_page_source

router = APIRouter()

@router.get('/room/{room_slug}')
async def room_detail(room_slug):
    return {
        'slug': room_slug
    }
