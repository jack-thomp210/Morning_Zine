import requests as rq
from bs4 import BeautifulSoup as bs
song = input("Enter song: ")

url_params = {"q": song.lower()}

geniuslyrics_search = rq.get("https://https://genius.com/search?", params=url_params)
soup = bs(geniuslyrics_search.text, "lxml")
