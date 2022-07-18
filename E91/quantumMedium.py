from flask import Flask, request
from qiskit import *
from tqdm import tqdm
from time import time

singlets_sent = 2000
qcomp = Aer.get_backend("qasm_simulator")
bases = {"alice": None, "bob": None, "eve": None}
results = None
singlets = []
chsh_res = None
chsh_corr_val = None

def alice_measure(qc, basis):  # basis = "X", "W" or "Z"
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

def bob_measure(qc, basis):  # basis = "W", "Z" or "V"
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
    global results, singlets, chsh_res
    alice_bases = bases["alice"]
    bob_bases = bases["bob"]
    eve_bases = bases["eve"]
    for i in tqdm(range(singlets_sent)):
        singlet = QuantumCircuit(2, 4)
        singlet.x(0)
        singlet.x(1)
        singlet.h(0)
        singlet.cx(0, 1)
        if eve_bases:
            # We are just adding the measurement of eve's qubit,
            # we won't make eve actually read them ever...
            # We only want eve to indulge...
            # in real scenario, eve will read them, but here she isn't
            alice_measure(singlet, eve_bases[i])
            # bob_measure(singlet, eve_bases[i])
        alice_measure(singlet, alice_bases[i])
        bob_measure(singlet, bob_bases[i])
        singlet.measure(0, 0)
        singlet.measure(1, 1)
        singlets.append(singlet)
    t0 = time()
    result = execute(singlets, qcomp, shots=1).result().get_counts()
    print(f"\ntook {time()-t0} seconds\n")
    chsh_res = result
    result = [list(x.keys())[0] for x in result]
    alice_result = "".join([x[-1] for x in result])
    bob_result = "".join([x[-2] for x in result])
    results = {"alice": alice_result, "bob": bob_result}

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
    return "Ok"

@app.route("/read_qubits", methods=["POST"])
def read_qubits():
    name = request.form["name"]
    if results:
        return results[name]
    else:
        return "wait"

app.run(
    host="localhost",
    port=5001,
    debug=True,
 )
