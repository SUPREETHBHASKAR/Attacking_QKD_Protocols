from random import choice as IDK
from random import sample as take_any
import requests
from time import sleep

name = "alice"
print(f"Hi! This is {name.title()}!")

qIP, qPORT = "localhost", "5050"
cIP, cPORT = "localhost", "5000"
quantumMedium  =  f"http://{qIP}:{qPORT}/"  # URL of quantum channel 
classicalMedium = f"http://{cIP}:{cPORT}/"  # URL of classical channel

def prepare(key_length):
    a = ""  # X or not
    b = ""  # H or not
    for i in range(key_length):
        a += IDK(["0", "1"])
        b += IDK(["+", "*"])
    return a, b

def sendQubit(key_length):
    bits, bases = prepare(key_length)
    requests.post(f"{quantumMedium}send_qubit",
                  data = {
                      "bits": bits,
                      "bases": bases,
                      "name": name
                      }
                  ).text
    return bits, bases

def get_bob_bases(bases):
    try:
        ret = requests.post(f"{classicalMedium}get_bob_bases", data = {"bases": bases}).text
    except:
        sleep(5)
        return get_bob_bases(bases)
    if  ret == "wait":
        sleep(5)
        return get_bob_bases(bases)
    return ret

def send_sample(usable_bits, n = 0.3):
    sample_indices = sorted(
        take_any(usable_bits, int((key_length/2)*n))
    )
    # print(len(sample_indices))
    sampleD = {x: bits[x] for x in sample_indices}
    
    # Encoding it before sending
    sample = ""
    for index, bit in sampleD.items():
        sample += f"{index}:{bit}-"
    sample = sample[:-1]
    # sending
    requests.post(f"{classicalMedium}send_sample", data = {"sample": sample}).text    
    
    return sampleD

def compile_key(bits, sample, usable_bits):
    use = [i for i in range(key_length) if i in usable_bits and i not in sample.keys()]
    ret = ""
    for i in use:
        ret += bits[i]
    return ret

key_length = int(requests.get(quantumMedium).text)

bits, alice_bases = sendQubit(key_length)

bob_bases = get_bob_bases(alice_bases)

# print(f"len(bob_bases) = {len(bob_bases)}")

usable_bits = [i for i in range(key_length) if bob_bases[i] == alice_bases[i]]

# print(sum(usable_bits))

sample = send_sample(usable_bits, n = 0.3)

key = compile_key(bits, sample, usable_bits)
print(f"key = {key}")