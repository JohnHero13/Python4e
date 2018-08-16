import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    # South Federal University"
    # Belarusian State University
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved:', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print ('----Failrure to retrieve-----')
        print(data)
        continue

    #print(json.dumps(js, indent=4)) to see the file in order to understand the structure of the site

    placeID = js['results'][0]['place_id']
    print('PlaceID', placeID)
    break

print(placeID)
