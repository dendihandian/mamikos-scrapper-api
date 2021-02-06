from fastapi import APIRouter
from bs4 import BeautifulSoup
from app.helpers.helper import get_page_source

router = APIRouter()


@router.get("/kampus")
async def kampus_list():
    page_source = get_page_source("/kampus")
    soup = BeautifulSoup(page_source, 'html.parser')

    ul_list = soup.find_all('ul', class_="area-group-list-item")

    data = list()

    for ul in ul_list:
        for li in ul:
            el = li.a
            data.append({
                "name": el['href'].split('/')[-1],
                "display_name": el.text.strip()
            })

    return data
