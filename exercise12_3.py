import urllib.request, urllib.parse, urllib.error
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#http://py4e-data.dr-chuck.net/comments_124882.html
html = urllib.request.urlopen(url, context=ctx).read() #gives us the whole file
#html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser') #reads the html-file in a new clean object

#retrieve all the anchor tags
count = 0
spans=soup('span')
for span in spans:
    count = count + int(span.contents[0])
print(count)
