from bs4 import BeautifulSoup

with open('result.html', 'r') as file:
    # data = file.read().replace('\n', '')
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
area_lists = soup.find_all('ul', class_="area-group-list-item")
# print(area_list)

for area_list in area_lists:
    for area in area_list:
        print(area.text.strip())
