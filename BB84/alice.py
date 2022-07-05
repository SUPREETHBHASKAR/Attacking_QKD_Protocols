from random import choice as IDK
import requests
from tqdm import tqdm



name = "alice"

qIP = "localhost"
cIP = "localhost"
quantumMedium  =  f"http://{qIP}:5050/"  # quantum channel in port 5050
classicalMedium = f"http://{cIP}:5000/"  # classical channel in port 5000

def prepare():
    a = IDK([0, 1])  # X or not
    b = IDK([0, 1])  # H or not
    # a, b = 1, 1
    basis = "+"
    if b: basis = "*"
    # print(f"Expected Output: {a} in {basis} basis!")
    return f"{a}{b}", str(a), basis

def sendQubit():
    instruction, a, b = prepare()
    result = requests.post(f"{quantumMedium}sendqubit", data = {"qubit": instruction, "name": name}).text
    return a, b, result

for i in tqdm(range(6)):
    val, basis, result = sendQubit()
    if result == "Key is full!":
        break