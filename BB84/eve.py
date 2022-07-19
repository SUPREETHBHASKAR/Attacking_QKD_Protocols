import requests
from random import choice as IDK
from time import sleep

name = "eve"
print(f"Hi! This is {name.title()}!")

qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

def readQubit():
    bases = ""
    for i in range(key_length):
        bases += IDK(["+", "*"])
    # print(basis)
    bits = requests.post(f"{quantumMedium}read_qubits", data = {"basis": bases}).text
    if bits == "Wait":
        print("waiting...")
        sleep(1)
        return readQubit()
    return [bits, bases]

key_length = int(requests.get(quantumMedium).text)

bits, bob_bases = readQubit()

print("completed eavesdropping!")