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
    """prepares key_length number of random choices for qubits
    to be prepared in. a denotes the values of the qubits and b
    denotes the corresponding bases to be used to encode the qubit"""
    a = ""  # X or not
    b = ""  # H or not
    for i in range(key_length):
        a += IDK(["0", "1"])
        b += IDK(["+", "*"])
    return a, b

def sendQubit(key_length):
    """gets the qubit preparation choices and sends them to quantum channel"""
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
        sleep(key_length/120)
        return get_bob_bases(bases)
    if  ret == "wait":
        sleep(key_length/120)
        return get_bob_bases(bases)
    return ret

def send_sample(usable_bits, n = 0.3):
    """prepares and sends a sample of the qubits to quantum channel"""
    sample_indices = sorted(
        take_any(usable_bits, int((key_length/2)*n))
    )
    print("sample length =", len(sample_indices))
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
    """compiles the key from the usable bits and discarding the sample"""
    use = [i for i in range(key_length) if i in usable_bits and i not in sample.keys()]
    ret = ""
    for i in use:
        ret += bits[i]
    return ret

def successful():
    try:
        ret = requests.get(f"{classicalMedium}status").text
    except:
        sleep(5)
        return successful()
    if  ret == "wait":
        sleep(5)
        return successful()
    if ret == "success":
        return True
    return False



# Know the key length
key_length = int(requests.get(quantumMedium).text)

# Send those many qubit preparation choices to quantum channel.
# Quantum channel will prepare them as requested
bits, alice_bases = sendQubit(key_length)

# Get the bases of Bob
bob_bases = get_bob_bases(alice_bases)

# know which qubits have been read by Bob in the correct basis
# to calculate which qubits are usable and which aren't
usable_bits = [i for i in range(key_length) if bob_bases[i] == alice_bases[i]]

# Send a sample of the usable qubits to quantum channel
sample = send_sample(usable_bits, n = 0.3)

# If successful, compile the key, else abort the mission
if successful():
    key = compile_key(bits, sample, usable_bits)
    print(f"key = {key}")
else:
    print("Eve Detected, mission abort!")