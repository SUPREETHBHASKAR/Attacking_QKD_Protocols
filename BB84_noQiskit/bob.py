import requests
from random import choice as IDK
from time import sleep
from tqdm import tqdm

name = "bob"

qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

key_length = int(requests.get(quantumMedium).text)

def readQubit():
    basis = ""
    for i in range(key_length):
        basis += IDK(["+", "*"])
    # print(basis)
    ans = requests.post(f"{quantumMedium}getqubit", data = {"basis": basis}).text
    if ans == "Wait":
        print("waiting...")
        sleep(1)
        return readQubit()
    return [ans, basis]

bits, bases = readQubit()

print(bases)
print(bits)