from module import *

name = "bob"
print(f"Hi! This is {name.title()}!")
baseOpt = ['W', 'Z', 'V']

number_of_singlets = int(requests.get(quantuMedium).text)
bob_bases = send_bases(baseOpt, number_of_singlets, name)
bits = measure_qubits(name)
alice_bases = get_alice_bases("".join(bob_bases))

key = ""
uBitsB = ""
for i in range(number_of_singlets):
    if bob_bases[i] == alice_bases[i]:
        bit = int(bits[i])
        if bit: key += "0"
        else: key += "1"
        uBitsB += " "
    else:
        uBitsB += bits[i]
        
key_length = len(key)
mismatch = number_of_singlets - key_length

uBitsA = get_alice_uBits(uBitsB)

chsh_score = chsh(uBitsA, uBitsB, alice_bases, bob_bases)
print(f"chsh score: {chsh_score}")
success = chsh_score < -2

if success:
    print(key)
else:
    print("Eve is here! Abort!")