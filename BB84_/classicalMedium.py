from flask import Flask, request

users = {}

app = Flask(__name__)


bob_bases, alice_bases = None, None
sample = None
status = None


@app.route('/get_bob_bases', methods=['POST'])
def get_bob_bases():
    global alice_bases
    alice_bases = request.form['bases']
    if bob_bases:
        return bob_bases
    return "wait"

@app.route('/get_alice_bases', methods=['POST'])
def get_alice_bases():
    global bob_bases
    bob_bases = request.form['bases']
    if alice_bases:
        return alice_bases
    return "wait"

@app.route("/send_sample", methods=["POST"])
def send_sample():
    global sample
    sample = request.form["sample"]
    return "Got it!"

@app.route("/get_sample")
def get_sample():
    if sample:
        return sample
    return "wait"

@app.route("/status", methods=["GET", "POST"])
def get_status():
    global status
    if request.method == "GET":
        if status != None:
            return status
        return "wait"
    else:
        status = request.form["status"]
        return "done"
        

app.run(
    # host = "192.168.0.100",
    host = "localhost",
	port = 5000,
	debug = True,
 )