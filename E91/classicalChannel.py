from flask import Flask, request

app = Flask(__name__)

bob_bases, alice_bases = None, None
bob_uBits, alice_uBits = None, None
status = None

@app.route('/get_bob_bases', methods=['POST'])
def get_bob_bases():
    global alice_bases
    alice_bases = request.form['bases']
    # print(f"alice_bases = {alice_bases}")
    if bob_bases:
        return bob_bases
    return "wait"

@app.route('/get_alice_bases', methods=['POST'])
def get_alice_bases():
    global bob_bases
    bob_bases = request.form['bases']
    # print(f"bob_bases = {bob_bases}")
    if alice_bases:
        return alice_bases
    return "wait"

@app.route('/get_bob_uBits', methods=['POST'])
def get_bob_uBits():
    global alice_uBits
    alice_uBits = request.form['uBits']
    # print(f"alice_uBits = {alice_uBits}")
    if bob_uBits:
        return bob_uBits
    return "wait"

@app.route('/get_alice_uBits', methods=['POST'])
def get_alice_uBits():
    global bob_uBits
    bob_uBits = request.form['uBits']
    # print(f"bob_uBits = {bob_uBits}")
    if alice_uBits:
        return alice_uBits
    return "wait"

app.run(
    host = "localhost",
    port = 5000,
    debug = True,
 )