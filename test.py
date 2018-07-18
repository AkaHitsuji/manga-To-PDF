# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'https://www.mangareader.net/fantasista'
#
# page = requests.get(base_url).text
# soup = BeautifulSoup(page, 'html.parser')
#
# image_url = soup.find_all('img')[0]['src']
#
# div_tags = soup.find_all('div', 'chico_manga')
#
# print(div_tags)


import re

url = 'https://www.mangareader.net/fantasista/1/2'
chapter_name = url.split("/")[3]
print(chapter_name)
