from flask import Flask, request

app = Flask(__name__)

bob_bases, alice_bases = None, None
bob_uBits, alice_uBits = None, None
status = None

@app.route('/get_bob_bases', methods=['POST'])
def get_bob_bases():
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
    global bob_bases
    bob_bases = request.form['bases']
    print(f"\nBob sent his bases and is requesting for Alice's bases.", end = " ")
    if alice_bases:
        print("The Classical Medium already has Alice's bases, so it gives it to him.")
        return alice_bases
    print("But Alice hasn't sent her bases yet, so he waits.")
    return "wait"

@app.route('/get_bob_uBits', methods=['POST'])
def get_bob_uBits():
    global alice_uBits
    alice_uBits = request.form['uBits']
    print(f"\nAlice sent her unused Bits and is requesting for Bob's unused Bits.", end = " ")
    if bob_uBits:
        print("The Classical Medium already has Bob's unused Bits, so it gives it to her.")
        return bob_uBits
    print("But Bob hasn't sent his unused Bits yet, so she waits.")
    return "wait"

@app.route('/get_alice_uBits', methods=['POST'])
def get_alice_uBits():
    global bob_uBits
    bob_uBits = request.form['uBits']
    print(f"\nBob sent his unused Bits and is requesting for Alice's unused Bits.", end = " ")
    if alice_uBits:
        print("The Classical Medium already has Alice's unused Bits, so it gives it to him.")
        return alice_uBits
    print("But Alice hasn't sent her unused Bits yet, so he waits.")
    return "wait"

app.run(
    host = "localhost",
    port = 5000,
    debug = True,
 )