import random
import requests
from time import sleep

qIP, qPORT = "10.1.55.133", "5050"
cIP, cPORT = "10.1.55.133", "5000"
charlie  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel


def send_bases(baseOpt, singlets_sent, name):
    choice = "".join([baseOpt[random.randint(0, len(baseOpt)-1)] for i in range(singlets_sent)])
    print("Sending bases...")
    requests.post(f"{charlie}send_bases",
                  data = {
                      "name": name,
                      "bases": choice,
                      }
                  ).text
    return choice

def read_qubits(name):
    try:
        print("Reading qubits...")
        ret = requests.post(f"{charlie}read_qubits", data={"name":name}).text
    except:
        sleep(10)
        return read_qubits(name)
    if  ret == "wait":
        sleep(10)
        return read_qubits(name)
    return ret

def get_bob_bases(bases):
    try:
        ret = requests.post(f"{classicalMedium}get_bob_bases", data = {"bases": bases}).text
    except:
        sleep(1)
        return get_bob_bases(bases)
    if  ret == "wait":
        sleep(1)
        return get_bob_bases(bases)
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

def chsh():
    try:
        ret = requests.get(f"{charlie}chsh").text
    except:
        sleep(1)
        return chsh()
    if  ret == "wait":
        sleep(1)
        return chsh()
    return ret