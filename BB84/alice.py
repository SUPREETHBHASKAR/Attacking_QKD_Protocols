from random import choice as IDK
import requests



name = "alice"

URL = f"http://localhost:5050/"

def prepare():
    a = IDK([0, 1])  # X or not
    b = IDK([0, 1])  # H or not
    # a, b = 1, 1
    basis = "+"
    if b: basis = "*"
    print(f"Expected Output: {a} in {basis} basis!")
    return f"{a}{b}", str(a), basis

def sendQubit():
    instruction, a, b = prepare()
    result = requests.post(f"{URL}sendqubit", data = {"qubit": instruction, "name": name}).text
    return a, b, result

while True:
    val, basis, result = sendQubit()
    if result == "Key is full!":
        break