import requests
from bs4 import BeautifulSoup
import settings
import urllib.request

img_link = []
full_img_link = []
request = requests.get(settings.full_url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
imgs = soup.find_all('div', {'class': 'catalog-element-media__thumb'})
print("Получаем относительные url")
for img in imgs:
    img_link.append(img.get('data-src'))
print("Получаем полные url")
for i in img_link:
    full_img_link.append(settings.url + i)

print("Начинаем закачку")

for url in full_img_link:
    print(f"Скачиваем изображение {url}")
    url = url.strip()
    file_name = url[url.rfind('/')+1:]
    img = urllib.request.urlopen(url).read()
    out = open(file_name, "wb")
    out.write(img)
    out.close()