from flask import Flask, request

app = Flask(__name__)

# Defining different values
bob_bases, alice_bases = None, None
sample = None
status = None

@app.route('/get_bob_bases', methods=['POST'])
def get_bob_bases():
    """Alice sends her bases and requests for Bob's bases.
    If Bob has already sent his bases, it returns the bases,
    otherwise, it returns "wait", so that Alice waits for 
    some time and comes back again to ask for Bob's bases."""
    global alice_bases
    alice_bases = request.form['bases']
    print(f"\nAlice sent her bases and is requesting for Bob's bases.", end = " ")
    if bob_bases:
        print("The Classical Medium already has Bob's bases, so it gives it to her.")
        return bob_bases
    print("But Bob hasn't sent his bases yet, so she waits.")
    return "wait"

@app.route('/get_alice_bases', methods=['POST'])
def get_alice_bases():
    """Similarly Bob sends his bases and requests for Alice's bases.
    If Bob has already sent his bases, it returns the bases, else returns "wait"."""
    global bob_bases
    bob_bases = request.form['bases']
    print(f"\nBob sent his bases and is requesting for Alice's bases.", end = " ")
    if alice_bases:
        print("The Classical Medium already has Alice's bases, so it gives it to him.")
        return alice_bases
    print("But Alice hasn't sent her bases yet, so he waits.")
    return "wait"

@app.route("/send_sample", methods=["POST"])
def send_sample():
    """Alice sends her sample."""
    global sample
    print(f"\nAlice sent her sample.")
    sample = request.form["sample"]
    return "Got it!"

@app.route("/get_sample")
def get_sample():
    """Bob requests for Alice's sample
    If Alice has sent her sample, it returns the sample, else returns "wait"."""
    print(f"\nBob is requesting for Alice's sample.", end = " ")
    if sample:
        print("The Classical Medium already has Alice's sample, so it gives it to him.")
        return sample
    print("But Alice hasn't sent her sample yet, so he waits.")
    return "wait"

@app.route("/status", methods=["GET", "POST"])
def get_status():
    """Bob after knowing Alice's sample, calculates the match factor.
    Depending upon the match factor he either decides to keep the key or not.
    He declares his decision in the classical Medium.
    Later Alice requests for the decision."""
    global status
    if request.method == "GET":
        print(f"\nAlice is requesting for Bob's decision on whether to proceed with the key or start the process of resending another key.")
        if status != None:
            print("The Classical Medium already has Bob's decision, so it gives it to her.")
            return status
        print("But Bob hasn't sent his decision yet, so she waits.")
        return "wait"
    else:
        print(f"\nBob is sending his decision on whether to proceed with the key or start the process of resending another key.")
        status = request.form["status"]
        return "done"

app.run(
    host = "localhost",  # change this to your local ip
	port = 5000,
	debug = True,
 )