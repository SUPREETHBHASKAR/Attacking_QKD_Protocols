from flask import Flask, request

app = Flask(__name__)

bob_bases, alice_bases = None, None
status = None

@app.route('/get_bob_bases', methods=['POST'])
def get_bob_bases():
    global alice_bases
    alice_bases = request.form['bases']
    print(f"alice_bases = {alice_bases}")
    if bob_bases:
        return bob_bases
    return "wait"

@app.route('/get_alice_bases', methods=['POST'])
def get_alice_bases():
    global bob_bases
    bob_bases = request.form['bases']
    print(f"bob_bases = {bob_bases}")
    if alice_bases:
        return alice_bases
    return "wait"

app.run(
    host = "10.1.55.133",
    port = 5000,
    debug = True,
 )