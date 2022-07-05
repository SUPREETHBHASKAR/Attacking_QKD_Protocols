import requests
from random import choice as IDK
from time import sleep

name = "eve"

qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

key_length = int(requests.get(quantumMedium).text)
