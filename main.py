import requests
from jsonExtract import jsonExtract

from pprint import pprint as print

city = "tashkent"

url = f"http://api.pray.zone/v2/times/today.json?city={city}&school=2"

r = requests.get(url)
# print(r.status_code)
namoz = r.json()['results']['datetime'][0]['times']
bomdod = r.json()['results']['datetime'][0]['times']['Fajr']
peshin = r.json()['results']['datetime'][0]['times']['Dhuhr']
asr = r.json()['results']['datetime'][0]['times']['Asr']
shom = r.json()['results']['datetime'][0]['times']['Maghrib']
xufton = r.json()['results']['datetime'][0]['times']['Isha']

print(f"Bomdod: {bomdod}")
print(f"Peshin: {peshin}")
print(f"Asr: {asr}")
print(f"Shom: {shom}")
print(f"Xufton: {xufton}")