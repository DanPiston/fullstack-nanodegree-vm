from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "F1OAP3TOGKR1HGKPVHV44NOZXRY0XSIA45MCUEWRZ13EJW43"
foursquare_client_secret = "MQFJB1QUTLDXAW3PSYUCSEUAJ2GVIXJDSBZNTBURJFQWCPHM"


def findARestaurant(mealType,location):
    coordinates = getGeocodeLocation(location)
    lat = coordinates[0]
    lng = coordinates[1]
    #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    #https://api.foursquare.com/v2/venues/search?v=20161016&ll=38.897478%2C%20-77.000147&query=donuts&intent=browse&radius=10&client_id=F1OAP3TOGKR1HGKPVHV44NOZXRY0XSIA45MCUEWRZ13EJW43&client_secret=MQFJB1QUTLDXAW3PSYUCSEUAJ2GVIXJDSBZNTBURJFQWCPHM
    url = ('https://api.foursquare.com/v2/venues/search?v=20161016&ll={}%2C%{}&query={}&intent=browse&radius=555&client_id={}&client_secret={}'.format(lat, lng, mealType, foursquare_client_id, foursquare_client_secret))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    print(result)

    #3. Grab the first restaurant
    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    #5. Grab the first image
    #6. If no image is available, insert default a image url
    #7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
    #findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")
