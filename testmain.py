"""Weather info from your IP"""

from pyowm import OWM
import json
from urllib3 import request as req

url = 'http://ipinfo.io/json'
response = req('GET', url)
data1 = response.data
data2 = json.loads(data1)

IP = data2['ip']
country = data2['country']
region = data2['region']
city = data2['city']

API = open('weather_API.txt').read()
owm = OWM(API)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Voronezh')
w = observation.weather

print('Weather in ' + region, ',', city, '\n', 't:', w.temperature('celsius')['temp'], '°',
      '\n', w.detailed_status, '\n', 'wind:', w.wind()['speed'], 'mps')
