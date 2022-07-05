import requests
from random import choice as IDK
from time import sleep
from tqdm import tqdm

name = "bob"

qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

def readQubit(qubitn):
    basis = IDK(["+", "*"])
    ans = requests.post(f"{quantumMedium}getqubit",
                        data = {
                            "qubitn": qubitn,
                            "basis": basis}
                        )
    return [ans.text, basis]


qubitn = 0

bases = ""
measurements = ""

while True:
    ans, basis = readQubit(qubitn)
    print(ans)
    if ans == "over": break
    elif ans == "wait a bit":
        sleep(1)
        print("waiting...")
        continue
    else:
        bases += basis
        measurements += ans
        qubitn += 1

print(bases)
print(measurements)