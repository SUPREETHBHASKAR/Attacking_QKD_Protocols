import requests
from random import choice as IDK
from time import sleep

name = "bob"
print(f"Hi! This is {name.title()}!")

qIP, qPORT = "localhost", "5050"
cIP, cPORT = "localhost", "5000"
quantumMedium  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel 
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel

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

def get_alice_bases(bases):
    try:
        ret = requests.post(f"{classicalMedium}get_alice_bases", data = {"bases": bases}).text
    except:
        sleep(1)
        return get_alice_bases(bases)
    if  ret == "wait":
        sleep(1)
        return get_alice_bases(bases)
    return ret

def get_sample():
    try:
        ret = requests.get(f"{classicalMedium}get_sample").text
    except:
        sleep(1)
        return get_sample()
    if  ret == "wait":
        sleep(1)
        return get_sample()
    return ret

def process_sample(sample):
    ss = sample.split("-")
    ret = {}
    for s in ss:
        a, b = s.split(":")
        ret[int(a)] = int(b)
    return ret

def compile_key(bits, sample, usable_bits):
    use = [i for i in range(key_length) if i in usable_bits and i not in sample.keys()]
    ret = ""
    for i in use:
        ret += bits[i]
    return ret

key_length = int(requests.get(quantumMedium).text)

bits, bob_bases = readQubit()

alice_bases = get_alice_bases(bob_bases)


usable_bits = [i for i in range(key_length) if bob_bases[i] == alice_bases[i]]

sample = process_sample(get_sample())

check = [sample[i] == int(bits[i]) for i in sample.keys()]

print(f"match = {sum(check)/len(check)*100}%")

if sum(check)/len(check)>=(0.9-0.05):
    requests.post(f"{classicalMedium}status", data = {"status": "success"})
    print("Success")
    key = compile_key(bits, sample, usable_bits)
    print(f"key length = {len(key)}")
    print(f"key = {key}")
else:
    requests.post(f"{classicalMedium}status", data = {"status": "abort"})
    print("Eve Detected, mission abort!")