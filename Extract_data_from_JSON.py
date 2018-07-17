import urllib.request, urllib.parse, urllib.error
import ssl
import json
 #Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location:- ')
print ('Retrieving ' + url)
data = urllib.request.urlopen(url, context=ctx).read()
print ('Retrieved %d characters' %len(data))
info = json.loads(data)
#print (info)
print('User count:', len(info['comments']))
sum = 0
for item in info['comments']:
    sum += item['count']
print('Sum:',sum)
