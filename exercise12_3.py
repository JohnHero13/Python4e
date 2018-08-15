import urllib.request, urllib.parse, urllib.error
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input('Enter position:'))-1 # position of the link
count = int(input('Enter count:'))+1 # number of times to be repeated
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#http://py4e-data.dr-chuck.net/known_by_Darragh.html
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read() #gives us the whole file
    soup = BeautifulSoup(html, 'html.parser') #reads the html-file in a new clean object
    href=soup('a')
    print(url)
    url = href[position].get("href", None)
