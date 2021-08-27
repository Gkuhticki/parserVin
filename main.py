import requests
from bs4 import BeautifulSoup
import settings

img_link = []
request = requests.get(settings.url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
imgs = soup.find_all('div', {'class': 'catalog-element-media__thumb'})
for img in imgs:
    img_link.append(img.get('data-src'))
