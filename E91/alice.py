from module import *

name = "alice"
print(f"Hi! This is {name.title()}!")
baseOpt = ['X', 'W', 'Z']

number_of_singlets = int(requests.get(quantuMedium).text)
alice_bases = send_bases(baseOpt, number_of_singlets, name)
bits = measure_qubits(name)
bob_bases = get_bob_bases("".join(alice_bases))

key = ""
uBitsA = ""
for i in range(number_of_singlets):
    if alice_bases[i] == bob_bases[i]:
        bit = int(bits[i])
        if bit: key += "1"
        else: key += "0"
        uBitsA += " "
    else:
        uBitsA += bits[i]
        
key_length = len(key)
mismatch = number_of_singlets - key_length

uBitsB = get_bob_uBits(uBitsA)

chsh_score = float(chsh(uBitsA, uBitsB, alice_bases, bob_bases))
print(f"chsh score: {chsh_score}")
success = chsh_score < -2

if success:
    print(key)
else:
    print("Eve is here! Abort!")