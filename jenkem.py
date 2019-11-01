import requests as rq
from bs4 import BeautifulSoup as bs
import csv

ingredients = rq.get("http://www.jenkemmag.com/home/")
soup = bs(ingredients.text, "lxml")

# This prints 5 links to the latest jenkem magazine articles.

def jenkem():
	csv_file = open('jenkem_scrape.csv','w')

	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['final_link', 'article_description'])


	for article in soup.find_all('li', class_='post-list-item', limit=10):
					
		for article_description in article('p', class_='post-listing-description'):
				#print(article_description.text) - used in next loop for formatting
				for article_url in article('a', class_='article-link'):
					final_link=article_url['href']
					#print(article_url.text) - Makes the output clunky. Title in URL
					#print(final_link)
					#print(article_description.text)
					#print('----------------------------------------------------------------------------------------')
					#print('\n')
					#print('========================================================================================')
					csv_writer.writerow([final_link, article_description.text])
	csv_file.close()				

#print('========================================================================================')
jenkem()