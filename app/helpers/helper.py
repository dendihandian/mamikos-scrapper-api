import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date

current_date = date.today().strftime('%Y_%m_%d')
options = Options()
options.headless = True
driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), options=options)

def get_page_source(url_context):
    url_context_slug = url_context.replace('/', '_')

    path_to_file = os.path.join(sys.path[0], 'page_resources', f'{current_date}{url_context_slug}.html')
    if os.path.exists(path_to_file):
        with open(f'page_resources/{current_date}{url_context_slug}.html', 'r', encoding="utf-8") as file:
            page_source = file.read()

        # files = [f for f in listdir(os.path.join(sys.path[0], 'page_resources'))]

    else:

        if not os.path.exists(os.path.join(sys.path[0], 'page_resources')):
            os.makedirs(os.path.join(sys.path[0], 'page_resources'))

        url = f'https://www.mamikos.com{url_context}'
        driver.get(url)
        page_source = driver.page_source

        with open(f'page_resources/{current_date}{url_context_slug}.html', 'w', encoding="utf-8") as file:
            file.write(page_source)

        driver.close()

    return page_source
