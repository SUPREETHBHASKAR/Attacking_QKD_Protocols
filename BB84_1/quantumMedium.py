from flask import Flask, request
from qiskit import *
from tqdm import tqdm

key_length = 2500
qubits = None
comp = Aer.get_backend("qasm_simulator")

def prepare(inp):
    """Prepares the qubits and returns a list of key_length quantum circuits."""
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
    """Measures the supplied qubit in the desired basis and returns the result."""
    if basis == "*":
        qc.h(0)
    elif basis != "+":
        raise ValueError('"basis" must be "+" or "*"!')
    qc.measure(0, 0)
    results = list(execute(qc, comp, shots = 1).result().get_counts().keys())[0]
    # if random() > 0.85: results = str(1-int(results))  # adding errors
    return results

def measure(qubits, mbasis):
    """takes all the qubits and all the bases and returns a string containing measurements."""
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
    """Anyone can know the key-length by raising a request to this endpoint."""
    print(f"someone asks for the key-length, Quantum Medium return {key_length}")    
    return str(key_length)

@app.route("/send_qubit", methods=["POST"])
def sendqubit():
    """
    Alice will send a dictionary of the form:
    data = {
            "bits": bits,  # key_length long string of 0s and 1s
            "bases": bases,  # key_length long string of + and *
            "name": name  # here name = "Alice"
            }

    this function will generate quantum circuits from then and store them in a list
    """
    global qubits
    name = request.form["name"]
    if name == "alice":
        print(f"\nAlice sends all the {key_length} qubit")
        qubits = prepare(request.form)
        return "Qubit Added"
    else:
        return f"{name.title()} is not authorised to send qubits!"

@app.route("/read_qubits", methods=["POST"])
def getqubit():
    """anyone can send a request along with a choice of bases at this
    endpoint to get the qubits read in that base."""
    if not qubits:
        print("\nSomeone sends bases and tries to measure the qubits. But Alice hasn't sent the Qubits yet! So he waits!")
        return "Wait"
    print("\nSomeone measures the qubits in his/her choice of bases.")
    bases = request.form["basis"]
    return measure(qubits, bases)

app.run(
    host = "localhost",  # change this to your local ip
	port = 5050,
	debug = True,
 )