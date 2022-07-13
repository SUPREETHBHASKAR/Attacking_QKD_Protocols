import random
import requests
from time import sleep


name = "bob"
print(f"Hi! This is {name.title()}!")

qIP, qPORT = "localhost", "5050"
cIP, cPORT = "localhost", "5000"
charlie  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel 
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel
baseOpt = ['W', 'Z', 'V']

singlets_sent = int(requests.get(charlie).text)

def send_bases():
    choice = "".join([baseOpt[random.randint(0, 2)] for i in range(singlets_sent)])
    requests.post(f"{charlie}send_bases",
                  data = {
                      "name": name,
                      "bases": choice,
                      }
                  ).text
    return choice

def read_qubits():
    try:
        ret = requests.post(f"{charlie}read_qubits", data={"name":name}).text
    except:
        sleep(5)
        return read_qubits()
    if  ret == "wait":
        sleep(5)
        return read_qubits()
    # return list(map(int, ret.split("|")))
    return ret

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













bob_bases = send_bases()
bits = read_qubits()
alice_bases = get_alice_bases("".join(bob_bases))

print(bits)

key = []  # {}

for i in range(singlets_sent):
    if alice_bases[i] == bob_bases[i]:
        bit = int(bits[i])
        if bit:
            key.append(-1)
        else:
            key.append(1)
        
key_length = len(key)

print(key_length*100/singlets_sent)
print(key)
