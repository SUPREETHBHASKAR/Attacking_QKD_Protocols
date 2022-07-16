from module import *

name = "bob"
print(f"Hi! This is {name.title()}!")
baseOpt = ['W', 'Z', 'V']

singlets_sent = int(requests.get(charlie).text)
bob_bases = send_bases(baseOpt, singlets_sent, name)
bits = read_qubits(name)
alice_bases = get_alice_bases("".join(bob_bases))

key = ""
for i in range(singlets_sent):
    if alice_bases[i] == bob_bases[i]:
        bit = int(bits[i])
        if bit: key += "1"
        else: key += "0"
        
key_length = len(key)
mismatch = singlets_sent - key_length
chsh_score = float(chsh())
print(f"chsh score: {chsh_score}")
success = chsh_score < 0.3-2**1.5

if success:
    print(key)
else:
    print("Eve is here! Abort!")