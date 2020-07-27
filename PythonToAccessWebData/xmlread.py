import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url= input ('Enter URL: ')  
# http://py4e-data.dr-chuck.net/comments_683656.xml/
#http://py4e-data.dr-chuck.net/comments_42.xml
uh = urllib.request.urlopen(url, context=ctx)
print('Retrieving:',url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)


results = tree.findall('comments/comment')

print('Count:',len(results))

suma =0
for item in results:
	suma = suma + int(item.find('count').text)


print(suma)



