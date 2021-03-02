import sys, pytz
from datetime import date
from astral.geocoder import database, lookup
from astral.sun import sun
from astral import LocationInfo
from geopy.geocoders import Nominatim

city_name = sys.argv[1]

try:
    city = lookup(city_name, database())
    print('Information for %s/%s\n' % (city.name, city.region))
except:
    print("This city is not available!")
    while True:
        ans = input("Add it to the database?(y/n) ")
        if ans == "y": break
        elif ans == "n": quit()
    timezone = input("Enter the timezone: ")
    geolocator = Nominatim(user_agent="iot-application")
    location = geolocator.geocode(city_name, language="en")
    city = LocationInfo(city_name, location.address, timezone, location.latitude, location.longitude)
    print('Information for %s\n' % (city.region))

timezone = city.timezone
print('Timezone: %s' % timezone)
print('Latitude: %.02f; Longitude: %.02f\n' % (city.latitude, city.longitude))
s = sun(city.observer, date=date.today(), tzinfo=pytz.timezone(timezone))
print('Dawn:    %s' % str(s['dawn']))
print('Sunrise: %s' % str(s['sunrise']))
print('Noon:    %s' % str(s['noon']))
print('Sunset:  %s' % str(s['sunset']))
print('Dusk:    %s' % str(s['dusk']))
