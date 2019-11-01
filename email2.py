import os
from smtplib import SMTP


EMAIL_ADDRESS = os.environ.get('GMAIL')
EMAIL_PASSWORD = os.environ.get('GMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	subject = 'test'
	body = 'test'

	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail(EMAIL_ADDRESS, 'jack.thomp210@gmail.com', msg)
