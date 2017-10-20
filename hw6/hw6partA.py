#Manali Desai


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "lxml")
tags = soup('span')
count = 0
s = 0
for tag in tags:
	count +=1
	s += int(tag.contents[0])

print(count)
print(s)


