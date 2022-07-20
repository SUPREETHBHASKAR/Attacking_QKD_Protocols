from flask import Flask, request
from qiskit import *

number_of_singlets = 500
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
    for i in range(number_of_singlets):
        singlet = QuantumCircuit(2, 4)
        singlet.x(0)
        singlet.x(1)
        singlet.h(0)
        singlet.cx(0, 1)
        if eve_bases:
            alice_measure(singlet, eve_bases[i])
            # bob_measure(singlet, eve_bases[i])
        alice_measure(singlet, alice_bases[i])
        bob_measure(singlet, bob_bases[i])
        singlet.measure(0, 0)
        singlet.measure(1, 1)
        singlets.append(singlet)
    result = execute(singlets, qcomp, shots=1).result().get_counts()
    chsh_res = result
    result = [list(x.keys())[0] for x in result]
    alice_result = "".join([x[-1] for x in result])
    bob_result = "".join([x[-2] for x in result])
    results = {"alice": alice_result, "bob": bob_result}

app = Flask(__name__)

@app.route("/")
def login():
    print(f"\nsomeone asked for the number of singlets... returned {number_of_singlets}")
    return str(number_of_singlets)

@app.route("/send_bases", methods=["POST"])
def send_bases():
    global bases
    name = request.form["name"]
    bases[name] = request.form["bases"]
    print(f"\n{name.title()} sent choice of bases")
    if bases["bob"] and bases["alice"]:
        print("\nAs the Quantum Medium has both the bases of Alice and Bob, it can start making measurements...")
        calc()
        print("\nmeasurements completed!")
    return "Ok"

@app.route("/measure_qubits", methods=["POST"])
def measure_qubits():
    name = request.form["name"]
    print(f"\n{name.title()} is requesting for the measurements.", end = " ")
    if results:
        print("Measurements are now ready, so Quantum Medium is  returning the results.")
        return results[name]
    else:
        print("But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!")
        return "wait"

app.run(
    host="localhost",
    port=5001,
    debug=True,
 )
