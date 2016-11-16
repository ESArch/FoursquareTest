import foursquare
import numpy as np

CLIENT_ID = "CY31BWAEIBASBKLWUURFUUN1W51HZNXTLGTICX2LCPFN0OMJ"
CLIENT_SECRET = "LG33GR15GKGXXFR1Z1ZDACTKOHXGCHUGHW310L2LC4BOOY04"

# Construct the client object
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

#sw = '-0.43,39.42'
#ne = '-0.29,39.50'

places = {}
repetidos = 0

latitudes = np.arange(39.42, 39.50, 0.01)
longitudes = np.arange(-0.43, -0.29, 0.01)

for lat in latitudes:
    for long in longitudes:
        ll = str(lat)+','+str(long)
        sw = str(lat)+','+str(long)
        ne = str(lat+0.01)+','+str(long+0.01)
        venues = client.venues.search(params={'ll': ll, 'sw': sw, 'ne': ne, 'limit': 50, 'categoryId':'4d4b7105d754a06374d81259,4d4b7104d754a06370d81259,4d4b7105d754a06373d81259,4d4b7105d754a06376d81259,4d4b7105d754a06377d81259,4bf58dd8d48988d12d941735'})['venues']

        for venue in venues:
            if venue['name'] in places.keys():
                repetidos += 1
                continue
            for category in venue['categories']:
                if category['primary'] == True:
                    places[venue['name']] = category['name']
                    break


f = open('places.txt', 'w', encoding='utf8')
for key,value in places.items():
    mystr = key + '\t' + value + '\n'
    f.write(mystr)

print(repetidos)

# Valencia
#venues = client.venues.search(params={'ll': '39.4,-0.35', 'radius': 5000, 'categoriesId': '4d4b7105d754a06374d81259', 'limit': 50})['venues']

# Madrid
#venues = client.venues.search(params={'ll': '40.4,-3.70', 'radius': 5000, 'intent':'browse', 'limit':50})['venues']

'''
for venue in venues:
    print(venue['name'],'\t',venue['categories'])

print(len(venues))
'''