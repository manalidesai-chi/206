import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Manali Desai

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = input('Enter count: ')
position = input('Enter position: ')


for i in range(int(count) + 1):
	print('Retriving: ' + url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	tags = soup('a')
	c = 0
	for tag in tags: #i in range(position):
		c += 1
		if c == int(position) :
			url = tag.get('href', None)
			break

