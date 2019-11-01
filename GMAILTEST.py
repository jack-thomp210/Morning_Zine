
import os
import smtplib
from email.message import EmailMessage
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

	csv_file = open('test_morningread.csv','w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['final_link', 'article_description','video_link.text', 'final_link', 'summary.text'])

	for article in soup.find_all('li', class_='post-list-item', limit=5):
		for article_description in article('p', class_='post-listing-description'):
				for article_url in article('a', class_='article-link'):
					final_link=article_url['href']
					csv_writer.writerow([final_link, article_description.text])
					

	for links in pasta.find_all('li', class_='post-list-item', limit=10):
		for video_link in links('a', class_='post-title-link'):
			
			final_link='https://www.thrashermagazine.com'+video_link['href']
					
		for summary in links('div', class_='post-description'):
			csv_writer.writerow([video_link.text, final_link, summary.text])
			
	csv_file.close()

morning_read()


EMAIL_ADDRESS = os.environ.get('GMAIL')
EMAIL_PASSWORD = os.environ.get('GMAIL_PASS')
'''
msg = EmailMessage()
msg['Subject'] = 'Test'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Attached are your articles.')

with open('test_morningread.csv', 'wb') as csvfile:
	reader = csv.DictReader(csvfile)
	
msg.add_attachment(reader, maintype='csv')	

def send_mail():
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		smtp.send_message(msg.as_string())
send_mail()
'''