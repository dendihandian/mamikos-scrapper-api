from fastapi import APIRouter
from bs4 import BeautifulSoup
from app.helpers.helper import get_page_source

router = APIRouter()


@router.get("/testimonials")
async def testimonial_list():
    data = list()
    page_source = get_page_source('/')
    soup = BeautifulSoup(page_source, 'html.parser')

    div_testimonial_wrapper = soup.find('div', class_='testimonial-wrapper')
    div_swiper_wrapper = div_testimonial_wrapper.find('div', class_='swiper-wrapper')

    for div_testimonial_item in div_swiper_wrapper:

        div_testimonial_identity = div_testimonial_item.find('div', class_='testimonial-identity')
        div_testimonial_content = div_testimonial_item.find('div', class_='testimonial-content')
        div_owner_image, div_owner_info = div_testimonial_identity.find_all('div')

        data.append({
            'image': div_owner_image['data-src'],
            'owner': div_owner_info.p.text.strip(),
            'kost': div_owner_info.h3.text.strip(),
            'content': div_testimonial_content.text.strip()
        })


    return data
