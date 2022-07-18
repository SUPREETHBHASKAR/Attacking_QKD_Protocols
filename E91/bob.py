from module import *

name = "bob"
print(f"Hi! This is {name.title()}!")
baseOpt = ['W', 'Z', 'V']

singlets_sent = int(requests.get(quantuMedium).text)
bob_bases = send_bases(baseOpt, singlets_sent, name)
bits = read_qubits(name)
alice_bases = get_alice_bases("".join(bob_bases))

# =============================
key = ""
uBitsB = ""
for i in range(singlets_sent):
    if bob_bases[i] == alice_bases[i]:
        bit = int(bits[i])
        if bit: key += "0"
        else: key += "1"
        uBitsB += " "
    else:
        uBitsB += bits[i]
        # uBits[i] = {alice_bases[i]: int(bits[i])}
        
key_length = len(key)
mismatch = singlets_sent - key_length
# =============================


uBitsA = get_alice_uBits(uBitsB)

print(f"uBitsA = {len(uBitsA)}")
print(f"uBitsB = {len(uBitsB)}")

chsh_score = chsh(uBitsA, uBitsB, alice_bases, bob_bases)
print(f"chsh score: {chsh_score}")
success = chsh_score < 0.3-2**1.5

if success:
    print(key)
else:
    print("Eve is here! Abort!")