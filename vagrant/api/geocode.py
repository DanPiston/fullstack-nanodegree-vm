import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyDCQpoMtKTye4Lk-0c5VODYuRs1Tiogo5M"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']
    return (lat, lng)
