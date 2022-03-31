# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import schedule
import time
import requests
import os
from dotenv import load_dotenv
load_dotenv()

prev = None
def job():
  global prev
  page_url = 'https://www.ai-yuma.com/'
  r  = requests.get(page_url)
  soup = BeautifulSoup(r.text, 'html.parser')
  img_tags = soup.find("img")
  url = img_tags.get("src")
  if url != prev:
    prev = url
    title = soup.find('a', class_= 'entry-title-link bookmark')
    print(url)
    return url, title.text
  return None, None

while True:
    discord_webhook_url = os.environ.get("WEB_HOOK")
    url, title = job()
    data = {"content": "ゆまAIが更新されました\n\n"+str(title)+str(url)}
    if url is not None:
      requests.post(discord_webhook_url, data=data)
    time.sleep(3)