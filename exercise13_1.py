import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter adress:')
html = urllib.request.urlopen(url, context=ctx).read()
# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_124884.xml

tree = ET.fromstring(html)
total = 0
lst = tree.findall('comments/comment/count')
print('User count', len(lst))

for count in lst:
    total += int(count.text)

print('Total:', total)
