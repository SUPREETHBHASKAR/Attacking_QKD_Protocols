import random
import requests
from time import sleep

qIP, qPORT = "localhost", "5001"
cIP, cPORT = "localhost", "5000"
quantuMedium  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel


def send_bases(baseOpt, number_of_singlets, name):
    choice = "".join([baseOpt[random.randint(0, len(baseOpt)-1)] for i in range(number_of_singlets)])
    print("Sending bases...")
    requests.post(f"{quantuMedium}send_bases",
                  data = {
                      "name": name,
                      "bases": choice,
                      }
                  ).text
    return choice

def measure_qubits(name):
    try:
        print("Reading qubits...")
        ret = requests.post(f"{quantuMedium}measure_qubits", data={"name":name}).text
    except:
        sleep(10)
        return measure_qubits(name)
    if  ret == "wait":
        sleep(10)
        return measure_qubits(name)
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

def get_bob_uBits(uBits):
    try:
        ret = requests.post(f"{classicalMedium}get_bob_uBits", data = {"uBits": uBits}).text
    except:
        sleep(1)
        return get_bob_uBits(uBits)
    if  ret == "wait":
        sleep(1)
        return get_bob_uBits(uBits)
    return ret

def get_alice_uBits(uBits):
    try:
        ret = requests.post(f"{classicalMedium}get_alice_uBits", data = {"uBits": uBits}).text
    except:
        sleep(1)
        return get_alice_uBits(uBits)
    if  ret == "wait":
        sleep(1)
        return get_alice_uBits(uBits)
    return ret

def chsh(uBitsA, uBitsB, alice_bases, bob_bases):
    search = ["00", "01", "10", "11"]  # f"{bob}{alice}"
    XW = [0, 0, 0, 0]
    XV = [0, 0, 0, 0]
    ZW = [0, 0, 0, 0]
    ZV = [0, 0, 0, 0]

    for i in range(len(alice_bases)):
        try:
            if uBitsA[i] == " ":
                continue
        except IndexError:
            raise IndexError(f"i = {i}")

        if alice_bases[i] == "X" and bob_bases[i] == "W":
            for j in range(4):
                if f"{uBitsA[i]}{uBitsB[i]}" == search[j]:
                    XW[j] += 1
                    break
        if alice_bases[i] == "X" and bob_bases[i] == "V":
            for j in range(4):
                if f"{uBitsA[i]}{uBitsB[i]}" == search[j]:
                    XV[j] += 1
                    break
        if alice_bases[i] == "Z" and bob_bases[i] == "W":
            for j in range(4):
                if f"{uBitsA[i]}{uBitsB[i]}" == search[j]:
                    ZW[j] += 1
                    break
        if alice_bases[i] == "Z" and bob_bases[i] == "V":
            for j in range(4):
                if f"{uBitsA[i]}{uBitsB[i]}" == search[j]:
                    ZV[j] += 1
                    break

    # expectation values of XW, XV, ZW and ZV observables (2)
    chsh_corr_val = [
                (XW[0] - XW[1] - XW[2] + XW[3]) / sum(XW),  # -1/sqrt(2)
                -(XV[0] - XV[1] - XV[2] + XV[3]) / sum(XV),  # 1/sqrt(2)
                (ZW[0] - ZW[1] - ZW[2] + ZW[3]) / sum(ZW),  # -1/sqrt(2)
                (ZV[0] - ZV[1] - ZV[2] + ZV[3]) / sum(ZV)  # -1/sqrt(2)
        ]

    chsh_corr_val = sum(chsh_corr_val)
    return chsh_corr_val
