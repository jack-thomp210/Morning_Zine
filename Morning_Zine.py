import os
import requests as rq
from bs4 import BeautifulSoup as bs
import csv


	
URL1 = "http://www.jenkemmag.com/home/"
URL2 = "https://thrashermagazine.com/most-recent/"


def morning_read():
	site1 = rq.get(URL1)
	site2 = rq.get(URL2)
	soup = bs(site1.text, 'lxml')
	pasta = bs(site2.text, 'lxml')

	csv_file = open('ZineLinks.csv','w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['final_link', 'article_description','video_link.text', 'final_link', 'summary.text'])

	# Grabbing the title for these links was a formatting nightmare. the title is in the url
	for article in soup.find_all('li', class_='post-list-item', limit=3): # Change the limit to the number of links you would like for this website.
		for article_description in article('p', class_='post-listing-description'):
				for article_url in article('a', class_='article-link'):
					final_link=article_url['href'] # Creates the full link
					csv_writer.writerow([final_link, article_description.text]) # Grabbing the title for these links was a formatting nightmare. the title is in the url
					print(final_link)
					print(article_description.text)
					print('========================================================================================')

	for links in pasta.find_all('li', class_='post-list-item', limit=3): # Change the limit to the number of links you would like for this website.
		for video_link in links('a', class_='post-title-link'):
			print(video_link.text)
			final_link='https://www.thrashermagazine.com'+video_link['href'] # Creates the full link
			print(final_link)		
		for summary in links('div', class_='post-description'):
			csv_writer.writerow([final_link, video_link.text])
			print(summary.text)
			print('========================================================================================')
	#csv_file.close()
print('========================================================================================')
morning_read()
print('========================================================================================')
print("Good morning.")
print("Your morning articles are in the ZineLinks.csv file.")
exit()






