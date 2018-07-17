import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:- ')
print ('Retrieving ' + url)
xml = urllib.request.urlopen(url, context=ctx).read()
print ('Retrieved %d characters' %len(xml))
stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
#print(lst)
print('User count:', len(lst))
#counts = stuff.findall('.//count')
#print('User Count:',len(counts))
sum = 0
for item in lst:

   #print('Name', item.find('name').text)
   sum += int(item.find('count').text)
print('Sum:',sum)
