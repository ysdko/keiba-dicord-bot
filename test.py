import requests
from bs4 import BeautifulSoup
import schedule
import time
page_url = 'https://www.ai-yuma.com/'
r  = requests.get(page_url)
soup = BeautifulSoup(r.text, 'html.parser')
img_tags = soup.find_all("img")
title = soup.find('a', class_= 'entry-title-link bookmark')
print(title.text)