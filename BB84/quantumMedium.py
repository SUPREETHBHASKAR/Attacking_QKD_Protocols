from flask import Flask, request
from random import choice as IDK
from qiskit import *

app = Flask(__name__)




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





@app.route("/send", methods=["POST"])
def alice():
    """
    Alice will send a dictionary of the form:
    qubit = {"qubit": "10"}  # 00, 01, 10 or 11
    First bit is X or not, second bit is H or not

    this function will store them in a list (list of dictionaries)
    """
    # ret = f"Request from Alice: {dict(request.form)}"
    qc = prepare(dict(request.form)["qubit"])
    result = measure(qc, "*")
    print(f"\n{result}\n")
    return "Thanks!"


# something here


app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5050,
	debug = True,
 )