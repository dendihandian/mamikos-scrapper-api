from fastapi import APIRouter
from bs4 import BeautifulSoup
from app.helpers.helper import get_page_source

router = APIRouter()

@router.get("/kost")
async def kost_list():
    page_source = get_page_source("/kost")
    soup = BeautifulSoup(page_source, 'html.parser')

    listing = soup.find('section', class_='listing-container')
    listing_div = listing.find('div', class_="row")

    # print(listing_div)

    data = list()

    for col_custom in listing_div:
        try:
            div_room_card = col_custom.find('div', class_='room-card')
            img_room_cover_mage = div_room_card.find('img', class_='room-cover-image')
            div_room_information_wrapper = div_room_card.find('div', class_='room-information-wrapper')
            div_room_title = div_room_information_wrapper.find('div', class_='room-title')
            div_room_tag_wrapper = div_room_information_wrapper.find('div', class_='room-tag-wrapper')
            div_room_location = div_room_information_wrapper.find('div', class_='room-location')
            div_room_meta_section = div_room_information_wrapper.find('div', class_='room-meta-section')
            div_real_price_container = div_room_meta_section.find('div', class_='real-price-container')
            p_real_price = div_real_price_container.find('p', class_='real-price')
            p_real_price_unit = div_real_price_container.find('p', class_='real-price-unit')
            div_room_meta = div_room_meta_section.find('div', class_='room-meta')
            span_rating = div_room_meta.find('span')

            data.append({
                'display_name':  div_room_title.h3.text.strip(),
                'gender': div_room_tag_wrapper.label.text.strip(),
                'location': div_room_location.span.text.strip(),
                'price': p_real_price.text.strip() + p_real_price_unit.text.strip(),
                'image': img_room_cover_mage['src'],
                'rating': float(span_rating.text.strip())
            })
        except:
            pass

    return data

@router.get('/kost/{kost_slug}')
async def kost_detail(kost_slug):
    return {
        'slug': kost_slug
    }