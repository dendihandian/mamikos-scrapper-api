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
            room_card = col_custom.find('div', class_='room-card')
            room_cover_mage = room_card.find('img', class_='room-cover-image')
            room_information_wrapper = room_card.find('div', class_='room-information-wrapper')
            room_title = room_information_wrapper.find('div', class_='room-title')
            room_tag_wrapper = room_information_wrapper.find('div', class_='room-tag-wrapper')
            room_location = room_information_wrapper.find('div', class_='room-location')
            room_meta_section = room_information_wrapper.find('div', class_='room-meta-section')
            real_price_container = room_meta_section.find('div', class_='real-price-container')
            real_price = real_price_container.find('p', class_='real-price')
            real_price_unit = real_price_container.find('p', class_='real-price-unit')
            room_meta = room_meta_section.find('div', class_='room-meta')
            rating_span = room_meta.find('span')

            data.append({
                'display_name':  room_title.h3.text.strip(),
                'gender': room_tag_wrapper.label.text.strip(),
                'location': room_location.span.text.strip(),
                'price': real_price.text.strip() + real_price_unit.text.strip(),
                'image': room_cover_mage['src'],
                'rating': float(rating_span.text.strip())
            })
        except:
            pass

    return data
