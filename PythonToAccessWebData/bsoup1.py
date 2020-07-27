import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name=list()

url= input ('Enter URL: ')
count=int(input('Enter count: '))
pos= int(input ('Enter position: '))

print('Retrieving:',url)
name.append(url)

while count >0:
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	#	 Retrieve all of the anchor tags
	tags = soup('a')
	suma=list()
	for tag in tags:
		suma.append(tag.get('href',None))


	url=suma[(pos)-1]
	print('Retrieving:',url)
	name.append(url)
	count = count-1


#print(name)

listname=list()

for x in name:
		ss=re.findall(r'known_by_(.*).html',x)
		listname.append(ss)

print(listname[len(listname)-1])
