import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter adress:')
print("Retrieving ", url)
data = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')
# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_124885.json
print(len(data), 'characters')

info = json.loads(data)
count = 0
Sum = 0

for item in info['comments']:
    count = count + 1
    x = int(item['count'])
    Sum = Sum +x
print(count)
print(Sum)
