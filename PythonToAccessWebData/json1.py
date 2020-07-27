import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_683657.json (Sum ends with 61)


url= input ('Enter URL: ')  
uh = urllib.request.urlopen(url, context=ctx)
print('Retrieving:',url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)


suma =0
for item in info['comments']:
  suma= suma + int( item['count'])
print(suma)