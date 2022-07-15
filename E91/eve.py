import random
import requests
from time import sleep


name = "eve"
print(f"Hi! This is {name.title()}!")

qIP, qPORT = "localhost", "5050"
cIP, cPORT = "localhost", "5000"
charlie  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel 
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel
baseOpt = ['W', 'Z']

singlets_sent = int(requests.get(charlie).text)

def send_bases(choices = 3):
    choice = "".join([baseOpt[random.randint(0, choices-1)] for i in range(singlets_sent)])
    requests.post(f"{charlie}send_bases",
                  data = {
                      "name": name,
                      "bases": choice,
                      }
                  ).text
    return choice

send_bases(2)