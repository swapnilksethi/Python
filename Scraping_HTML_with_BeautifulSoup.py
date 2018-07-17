import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
#print (html)
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
result = 0
count=0
for value in re.findall('[0-9]+</span>', str(soup)):
	for x in re.findall('[0-9]+',value):
	    #print (x)
	    count +=1
	    result += int(x)	
print('Count: %d'%count)
print('Sum is: %d' %result)
