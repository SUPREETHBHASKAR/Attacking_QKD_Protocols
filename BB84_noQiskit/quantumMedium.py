from flask import Flask, request
from qiskit import *
from random import choice as IDK
from random import random
from tqdm import tqdm
# from time import sleep

key_length = 10000
qubits = None
comp = Aer.get_backend("qasm_simulator")

def prepare(inp):
    bits = inp["bits"]
    bases = inp["bases"]
    message = []
    for i in tqdm(range(key_length)):
        qc = QuantumCircuit(1,1)
        if int(bits[i]): qc.x(0)
        if bases[i] == "*": qc.h(0)
        qc.barrier()
        message.append(qc)
    return message

def measure1(qc, basis):
    if basis == "*":
        qc.h(0)
    elif basis != "+":
        raise ValueError('"basis" must be "+" or "*"!')
    qc.measure(0, 0)
    results = list(execute(qc, comp, shots = 1).result().get_counts().keys())[0]
    if random() > 0.9: results = str(1-int(results))  # adding errors
    return results

def measure(qubits, mbasis):
    if len(qubits) != len(mbasis):
        raise ValueError(f"length of qubits (= {len(qubits)}) and length of mbasis (= {len(mbasis)}) aren't equal")
    ret = ""
    for i in tqdm(range(len(mbasis))):
        qc = qubits[i]
        basis = mbasis[i]
        ret += measure1(qc, basis)
    return ret

app = Flask(__name__)

@app.route("/")
def login():
    return str(key_length)

@app.route("/sendqubit", methods=["POST"])
def sendqubit():
    """
    Alice will send a dictionary of the form:
    qubit = {"qubit": "10"}  # 00, 01, 10 or 11
    First bit is X or not, second bit is H or not

    this function will generate quantum circuits from then and store them in a list
    """
    global qubits
    name = request.form["name"]
    if name == "alice":
        # ret = f"Request from Alice: {request.form}"
        qubits = prepare(request.form)
        return "Qubit Added"
    else:
        return f"{name.title()} is not authorised to send qubits!"

@app.route("/getqubit", methods=["POST"])
def getqubit():
    if not qubits:
        return "Wait"
    basis = request.form["basis"]
    # print("basis:", basis)
    return measure(qubits, basis)
    


# something here


app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5050,
	debug = True,
 )