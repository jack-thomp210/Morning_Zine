import requests as rq
from bs4 import BeautifulSoup as bs
import csv

stuff = rq.get("https://thrashermagazine.com/most-recent/")
soup = bs(stuff.text, "lxml")


# This gives you 5 titles, summaries, and links to Thrasher's most recent page.

def thrasher():
	csv_file = open('article_scrape.csv','w')

	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['video_link.text', 'final_link', 'summary.text'])


	for links in soup.find_all('li', class_='post-list-item', limit=5):
		for video_link in links('a', class_='post-title-link'):
			#print(video_link.text)
			final_link='https://www.thrashermagazine.com'+video_link['href']
			#print(final_link)
		
		for summary in links('div', class_='post-description'):
			#print(summary.text)
			#print('========================================================================================')
			csv_writer.writerow([video_link.text, final_link, summary.text])


#print('========================================================================================')
thrasher()