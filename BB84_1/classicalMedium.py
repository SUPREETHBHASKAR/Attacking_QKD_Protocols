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
    if bob_bases:
        return bob_bases
    return "wait"

@app.route('/get_alice_bases', methods=['POST'])
def get_alice_bases():
    """Similarly Bob sends his bases and requests for Alice's bases.
    If Bob has already sent his bases, it returns the bases, else returns "wait"."""
    global bob_bases
    bob_bases = request.form['bases']
    if alice_bases:
        return alice_bases
    return "wait"

@app.route("/send_sample", methods=["POST"])
def send_sample():
    """Alice sends her sample."""
    global sample
    sample = request.form["sample"]
    return "Got it!"

@app.route("/get_sample")
def get_sample():
    """Bob requests for Alice's sample
    If Alice has sent her sample, it returns the sample, else returns "wait"."""
    if sample:
        return sample
    return "wait"

@app.route("/status", methods=["GET", "POST"])
def get_status():
    """Bob after knowing Alice's samplle, calculates the match factor.
    Depending upon the match factor he either decides to keep the key or not.
    He declares his decission in the classical Medium.
    Later Alice requests for the decission."""
    global status
    if request.method == "GET":
        if status != None:
            return status
        return "wait"
    else:
        status = request.form["status"]
        return "done"

app.run(
    host = "localhost",  # change this to your local ip
	port = 5000,
	debug = True,
 )