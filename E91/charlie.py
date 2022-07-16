from flask import Flask, request
from qiskit import *
from tqdm import tqdm

singlets_sent = 1000
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
    result = execute(singlets, qcomp, shots=1).result().get_counts()
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

@app.route("/chsh")
def chsh():
    """Calculate the chsh correlation value of the measurements"""
    global chsh_corr_val
    if chsh_corr_val:
        return str(round(chsh_corr_val, 3))
    if not chsh_res:
        return "wait"
    # lists with the counts of measurement results
    search = ["00", "01", "10", "11"]
    XW = [0, 0, 0, 0]
    XV = [0, 0, 0, 0]
    ZW = [0, 0, 0, 0]
    ZV = [0, 0, 0, 0]

    for i in range(singlets_sent):

        res = list(chsh_res[i].keys())[0]

        if bases["alice"][i] == "X" and bases["bob"][i] == "W":
            for j in range(4):
                if res.endswith(search[j]):
                    XW[j] += 1
        if bases["alice"][i] == "X" and bases["bob"][i] == "V":
            for j in range(4):
                if res.endswith(search[j]):
                    XV[j] += 1
        if bases["alice"][i] == "Z" and bases["bob"][i] == "W":
            for j in range(4):
                if res.endswith(search[j]):
                    ZW[j] += 1
        if bases["alice"][i] == "Z" and bases["bob"][i] == "V":
            for j in range(4):
                if res.endswith(search[j]):
                    ZV[j] += 1

    # expectation values of XW, XV, ZW and ZV observables (2)
    chsh_corr_val = [
                (XW[0] - XW[1] - XW[2] + XW[3]) / sum(XW),  # -1/sqrt(2)
                -(XV[0] - XV[1] - XV[2] + XV[3]) / sum(XV),  # 1/sqrt(2)
                (ZW[0] - ZW[1] - ZW[2] + ZW[3]) / sum(ZW),  # -1/sqrt(2)
                (ZV[0] - ZV[1] - ZV[2] + ZV[3]) / sum(ZV)  # -1/sqrt(2)
        ]

    chsh_corr_val = sum(chsh_corr_val)
    return str(round(chsh_corr_val, 3))

app.run(
    host="10.1.55.133",
    port=5050,
    debug=True,
 )
