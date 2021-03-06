from fastapi import APIRouter
from bs4 import BeautifulSoup
from app.helpers.helper import get_page_source

router = APIRouter()

@router.get("/area")
async def area_list():
    page_source = get_page_source("/area")
    soup = BeautifulSoup(page_source, 'html.parser')

    ul_list = soup.find_all('ul', class_="area-group-list-item")

    # print(ul_list)

    data = list()

    for ul in ul_list:
        for li in ul:
            el = li.a
            data.append({
                "name": el['href'].split('/')[-1],
                "display_name": el.text.strip()
            })

    return data
