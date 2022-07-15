# Simulating BB84

&emsp; We are trying to implement BB84 Quantum Key Distribution protocol in Python. We plan to use **Flask** and **Qiskit** libraries of Python to achieve this.

## Files

&emsp; Description of all the files in this folder:

### Important Files

&emsp; We have five important files:

1. [**"quantumMedium.py":**](/quantumMedium.py) This is the quantum medium through which the 3 three parties (Alice, Bob and Eve) will communicate with each other.
2. [**"classicalMedium.py":**](/classicalMedium.py) This is the classical medium through which the 3 three parties (alice, bob and eve) will communicate with each other after they have communicated the qubit away.
3. [**"alice.py":**](/alice.py) This is Alice. She will use this code to carry out the communication throught the two above mentioned mediums.
4. [**"bob.py":**](/bob.py) Similarly this is the code for Bob.
5. [**"eve.py":**](/eve.py) Similarly this is the code for Eve.

### Not-so-Important Files

&emsp; We have two more Not-so-Important files.

1. [**"README.md":**](/README.md) It is this file!
2. [**"tries.ipynb":**](/tries.ipynb) I used this jupyter notebook to write all the trash codes to try out things.

## About BB84

&emsp; BB84 is a QKD Protocol based on the quantum phenomenon of **superposition**. According to Google, **"superposition is the ability of a quantum system to be in multiple states at the same time until it is measured"**. Here Alice will send qubits to Bob through a quantum channel. If Eve tries to evesdrop on the channel, Alice and Bob have a process by which they will be able to detect the presence of Eve in the channel. Hence they will discard the transmitted key and try again to evade Eve.

### Steps

1. Alice will prepare the qubits in either of two bases (+ or ×). The idea is, if the person who measures the qubit, measures it in the right basis (the same basis it was prepared in), he will have a *100% chance of reading its value (either 0 or 1) correctly. If a qubit is measured in the wrong basis, he will get a random result out of 0 and 1.
2. Alice sends these prepared qubits to Bob throught a quantum medium.
3. Bob doesn't know which qubit was prepared in which basis. So everytime while reading a qubit, he randomly chooses a basis and measures the qubit in that randomly chosen basis. Note that, as there are only 2 bases in which Alice can prepare the qubits, Bob, while reading will have 50% chance of reading a qubit in its correct basis.
4. Now, after the Qubits have been read, and destroyed, so that no one can measure them any more, Bob tells Alice the bases in which he measured which qubit. He uses a classical channel to do this. Alice also tells Bob the bases she used to prepare the qubits over the same classical channel. So, both of them know which qubits were measured in the correct base and which weren't. So, now they decide to discard the qubits which were measured in the wrong base and proceed with the ones which are guaranteed to be measured correctly. Note that, the classical medium is a public medium in which everyone can see everyone else's message, but, there is no way, they can impersonate one-another.
5. If everything had gone correctly till this point, and Eve hasn't done any of his mischievous activities, Alice and Bob should have two identical keys with them. So, just to verify this fact, Alice randomly chooses some of her bits, and reveals them to Bob through the classical channel. Bob, compares them with his own bits.
6. If Eve wasn't there, Bob must have got a *100% match. Else, if Bob measures a reduced match percentage, he can conclude that Eve must have indulged into the process.

**How Eve can try to Evesdrop:**

7. Suppose Eve intercepts the quantum medium and measures the qubits in some random choice of basis before Bob. So, she has a 50% chance of reading the qubits in its correct basis. Now, if Eve doesn't read a qubit in ist correct basis, she is bound to disturb its state. The qubit will collapse to the value she reads and in the basis she reads it.
8. Now, let us fast forward to step 5, Bob, compares Alice's sample with his own. Now, among the bases measured in the same basis as Alice had prepared it, Bob will measure the qubits and get the correct value if and only if Eve has also measured them in the correct basis. Chance of that to happen is 50%. So, while doing step 6, if Bob finds that the sample sent by Alice matches his one only by around 50% (which was supposed to be a *100% match), he will declare that the Key was compromised, and the process will again start from step 1.

 \* **100%:** This value is theoretically 100%, but practically this value goes down by some percentages due to errors in quantum systems.

### Explanation for the Code

![BB84 Protocol Schematic](ref/Flow_Chart.png)

 1. Alice asks Quantum Medium to get the length of the Key to be sent.
 2. Alice sends that many number of qubits to the quantum medium.
 2.5. (Optional) Eve can ask the Quantum medium for the length of the Key and send those many bases to Quantum Medium to be read.
 3. Bob asks Quantum Medium to get the length of the Key to be read.
 4. Bob sends those many choices of bases to quantum medium. The quantum medium reads those bases in the desired medium and returns them to Bob.
 5. Alice sends her bases to the Classical Medium, and in return gets Bob's bases
 6. Bob also sends his, and in return he gets Alice's bases. (Note, suppose Alice requests the server for Bob's bases by giving her own bases, but Bob hasn't given his bases to the classical medium yet. So, classical medium will make Alice wait till Bob sends his bases)
 7. Make a sample of bases-value pair.
 8. Send the Sample to Classical Medium.
 9. Bob gets the sample from Classical Medium.
 10. Bob matches his own qubits with the sample of Alice.
 11. Bob decides whether to Abort or to Use the Key. He tells his decission to the Classical Medium
 12. Alice gets to know about the decission made by Bob.
 13. Alice acts accordingly.