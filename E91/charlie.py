from flask import Flask, request
from qiskit import *
from tqdm import tqdm

singlets_sent = 1000
qcomp = Aer.get_backend("qasm_simulator")
bases = {"alice": None, "bob": None}
results = None
singlets = []


def alice_measure(qc, basis): # basis = "X", "W" or "Z"
    """Alice's measurement circuits"""

    if basis == "X":  # X basis
        qc.h(0)

    elif basis == "W":  # W basis
        qc.s(0)
        qc.h(0)
        qc.t(0)
        qc.h(0)

    elif basis == "Z":  # Z basis
        pass

    else:
        raise ValueError("Value of parameter 'basis' can be one of 'X', 'W' or 'Z'")

def bob_measure(qc, basis): # basis = "W", "Z" or "V"
    """Bob's measurement circuits"""

    if basis == "W":  # W basis
        qc.s(1)
        qc.h(1)
        qc.t(1)
        qc.h(1)

    elif basis == "Z":  # Z basis
        pass

    elif basis == "V":  # V basis
        qc.s(1)
        qc.h(1)
        qc.tdg(1)
        qc.h(1)

    else:
        raise ValueError("Value of parameter 'basis' can be one of 'W', 'Z' or 'V'")

def calc():
    global results, singlets
    alice_bases = bases["alice"]
    bob_bases = bases["bob"]
    for i in tqdm(range(singlets_sent)):
        singlet = QuantumCircuit(2, 4)
        singlet.x(0)
        singlet.x(1)
        singlet.h(0)
        singlet.cx(0, 1)
        alice_measure(singlet, alice_bases[i])
        bob_measure(singlet, bob_bases[i])
        singlet.measure(0, 0)
        singlet.measure(1, 1)
        singlets.append(singlet)
    result = execute(singlets, qcomp, shots = 1).result().get_counts()
    result = [list(x.keys())[0] for x in result]
    alice_result = "".join([x[-1] for x in result])
    bob_result = "".join([x[-2] for x in result])
    results = {"alice": alice_result, "bob": bob_result}
    

def chsh_corr():
    countA1B1 = [0, 0, 0, 0] # XW observable
    countA1B3 = [0, 0, 0, 0] # XV observable
    countA3B1 = [0, 0, 0, 0] # ZW observable
    countA3B3 = [0, 0, 0, 0] # ZV observable
    
    for i in range(singlets_sent):
        






app = Flask(__name__)

@app.route("/")
def login():
    return str(singlets_sent)

@app.route("/send_bases", methods=["POST"])
def send_bases():
    global bases
    name = request.form["name"]
    bases[name] = request.form["bases"]
    if bases["bob"] and bases["alice"]:
        calc()
    # print(f"bases = {bases}")
    return "Ok"

@app.route("/read_qubits", methods=["POST"])
def read_qubits():
    name = request.form["name"]
    if results:
        return results[name]
    else:
        return "wait"


    















app.run(
    # host = "192.168.0.100",
    host = "localhost",
    port = 5050,
    debug = True,
 )