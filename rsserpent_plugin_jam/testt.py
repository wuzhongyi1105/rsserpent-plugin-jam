import requests
import time
from bs4 import BeautifulSoup
import arrow
from rsserpent.utils import cached, Browser

index_url = "https://www.jsmsg.com/news/library.aspx"
session = requests.Session()
index_response = session.get(index_url)
urls = BeautifulSoup(index_response.text, "html.parser").select('#form1 > div.library-all.w11.wow.fadeInDown.animated > ul > li > a')
print (urls)
""" 
url = "https://www.jsmsg.com/news/detail.aspx?id=456"
text_response = session.get(url)
text = BeautifulSoup(text_response.text, "html.parser").select('#form1 > div.news-detail.w33.wow.fadeInDown.animated > div')

print (text) """