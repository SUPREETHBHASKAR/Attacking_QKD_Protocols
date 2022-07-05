from random import choice as IDK
import requests
from time import sleep

name = "alice"
qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

def prepare(key_length):
    a = ""  # X or not
    b = ""  # H or not
    for i in range(key_length):
        a += IDK(["0", "1"])
        b += IDK(["+", "*"])
    return a, b

def sendQubit(key_length):
    bits, bases = prepare(key_length)
    requests.post(f"{quantumMedium}sendqubit",
                  data = {
                      "bits": bits,
                      "bases": bases,
                      "name": name
                      }
                  ).text
    return bits, bases

key_length = int(requests.get(quantumMedium).text)

val, base = sendQubit(key_length)

while True:
    try:
        requests.get(classicalMedium, data = {"name": name}).text
        break
    except:
        print("Waiting for Classical Medium!")
        sleep(10)

