import requests
import time
from bs4 import BeautifulSoup
import arrow
from rsserpent.utils import cached

path = "/jam"


@cached
async def provider() -> dict:    
    # init List
    title_list = []
    url_list = []
    date_list = []
    text_list = []

    index_url = "https://www.jsmsg.com/news/library.aspx"
    session = requests.Session()
    index_response = session.get(index_url)
    urls = BeautifulSoup(index_response.text, "html.parser").select("#form1 > div.library-all.w11.wow.fadeInDown.animated > ul > li > a")
    title = BeautifulSoup(index_response.text, "html.parser").select("#form1 > div.library-all.w11.wow.fadeInDown.animated > ul > li > a > div.library-fr > h4")
    date = BeautifulSoup(index_response.text, "html.parser").select("#form1 > div.library-all.w11.wow.fadeInDown.animated > ul > li > a > div.library-fr > span")

    for g in range( 0, 9 ):
        # Get Title
        title_list.append( title[g].string )
        # Get and Formate Date
        pub_date = arrow.get( date[g].string[2:] )
        date_list.append(pub_date)
        # Get URL
        url = 'https://www.jsmsg.com/news/' + urls[g].attrs['href']
        url_list.append(url)
        # Get Content
        text_response = session.get(url)
        text = BeautifulSoup(text_response.text, "html.parser").select('#form1 > div.news-detail.w33.wow.fadeInDown.animated > div')
        text_list.append(text)


    return {
        "title": "江苏省美术馆",
        "link": "https://www.jsmsg.com/news/library.aspx",
        "description": "江苏省美术馆-馆内资讯",
        "items": [
            {
                "title": title_list[r],
                "description": text_list[r],
                "link": url_list[r],
                "pub_date": date_list[r],
            }
            for r in range(0, 9)
        ],
    }
