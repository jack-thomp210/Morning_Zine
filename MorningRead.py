import requests as rq
from bs4 import BeautifulSoup as bs

print("Good morning, Jack.")
print("Here are your morning articles.")
	
URL1 = "http://www.jenkemmag.com/home/"
URL2 = "https://thrashermagazine.com/most-recent/"


def Jenkem():
	site = rq.get(URL1)
	soup = bs(site.text, 'lxml')

	for article in soup.find_all('li', class_='post-list-item', limit=5):
		for article_description in article('p', class_='post-listing-description'):
				for article_url in article('a', class_='article-link'):
					final_link=article_url['href']
					print(final_link)
					print(article_description.text)
					print('========================================================================================')
					
def Thrasher():
	link = rq.get(URL2)
	soup = bs(link.text, "lxml")

	for links in soup.find_all('li', class_='post-list-item', limit=10):
		for video_link in links('a', class_='post-title-link'):
			print(video_link.text)
			final_link='https://www.thrashermagazine.com'+video_link['href']
			print(final_link)
		
		for summary in links('div', class_='post-description'):
			print(summary.text)
			print('========================================================================================')
print('========================================================================================')
Jenkem()
print('========================================================================================')
Thrasher()
