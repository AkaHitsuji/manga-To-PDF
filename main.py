import requests
from bs4 import BeautifulSoup

# get image url
base_url = 'https://www.mangareader.net/fantasista/1/2'
page = requests.get(base_url).text
soup = BeautifulSoup(page, 'html.parser')
image_url = soup.find_all('img')[0]['src']

# download image from image url
try:
    r = requests.get(image_url)
    r.raise_for_status()
    img_data = requests.get(image_url).content
    with open('test_image', 'wb') as handler:
        handler.write(img_data)
    print("image downloaded")
except requests.exceptions.RequestException as e:
    print(e)
    print("image was not downloaded")


print(image_url)
