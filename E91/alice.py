from module import *

name = "alice"
print(f"Hi! This is {name.title()}!")
baseOpt = ['X', 'W', 'Z']

singlets_sent = int(requests.get(quantuMedium).text)
alice_bases = send_bases(baseOpt, singlets_sent, name)
bits = read_qubits(name)
bob_bases = get_bob_bases("".join(alice_bases))


# =============================
key = ""
uBitsA = ""
for i in range(singlets_sent):
    if alice_bases[i] == bob_bases[i]:
        bit = int(bits[i])
        if bit: key += "1"
        else: key += "0"
        uBitsA += " "
    else:
        uBitsA += bits[i]
        # uBits[i] = {alice_bases[i]: int(bits[i])}   
        
key_length = len(key)
mismatch = singlets_sent - key_length
# =============================


uBitsB = get_bob_uBits(uBitsA)

chsh_score = float(chsh(uBitsA, uBitsB, alice_bases, bob_bases))
print(f"chsh score: {chsh_score}")
success = chsh_score < 0.3-2**1.5

if success:
    print(key)
else:
    print("Eve is here! Abort!")