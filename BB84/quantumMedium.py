from flask import Flask, request
from qiskit import *
from time import sleep

key_length = 5
qubits = []

def prepare(instruction):
    a = int(instruction[0])  # X or not
    b = int(instruction[1])  # H or not
    qc = QuantumCircuit(1, 1)
    basis = "+"
    if a:
        qc.x(0)
    if b:
        qc.h(0)
        basis = "*"
    # print(f"Expected Output: {a} in {basis} basis!")
    return qc

def measure(qc, basis):
    if basis == "*":
        qc.h(0)
    elif basis != "+":
        raise ValueError('"basis" must be "+" or "*"!')
    qc.measure(0, 0)

    comp = Aer.get_backend("qasm_simulator")
    results = list(execute(qc, comp, shots = 1).result().get_counts().keys())[0]
    return results

app = Flask(__name__)

@app.route("/sendqubit", methods=["POST"])
def sendqubit():
    """
    Alice will send a dictionary of the form:
    qubit = {"qubit": "10"}  # 00, 01, 10 or 11
    First bit is X or not, second bit is H or not

    this function will generate quantum circuits from then and store them in a list
    """
    name = request.form["name"]
    if name == "alice":
        if len(qubits) == key_length:
            return "Key is full!"
        # ret = f"Request from Alice: {request.form}"
        qc = prepare(request.form["qubit"])
        qubits.append(qc)
        return "Qubit Added"
    else:
        return f"{name.title()} is not authorised to send qubits!"

@app.route("/getqubit", methods=["POST"])
def getqubit():
    qubitn = int(request.form["qubitn"])
    if qubitn >= key_length:
        print(len(qubits))
        return "over"
    elif qubitn > len(qubits):
        print(qubitn, len(qubits))
        return "wait a bit"
    basis = request.form["basis"]
    print("basis:", basis)
    print("qubitn:", qubitn)
    return measure(qubits[qubitn], basis)
    


# something here


app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5050,
	debug = True,
 )