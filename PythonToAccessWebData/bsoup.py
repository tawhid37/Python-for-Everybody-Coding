import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl


ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verfy_mode= ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_683654.html'
html= urllib.request.urlopen(url,context=ctx).read()
soup =BeautifulSoup(html,'html.parser')

tags= soup('tr')

asum=0

suma=list()
for cell in tags:
	tt= cell.find_all('td')[1]
	suma.append(tt.text)


suma.remove('Comments')

for val in suma:
	asum = asum + int (val)

print(asum)
