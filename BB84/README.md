# Simulating BB84
&emsp; We are trying to implement BB84 Quantum Key Distribution protocol in Python. We plan to use **Flask** and **Qiskit** libraries of Python to achieve this.


## Files
&emsp; Description of all the files in this folder:

### Important Files
&emsp; We have five important files:
1. [**"quantumMedium.py":**](./quantumMedium.py) This is the quantum medium through which the 3 three parties (Alice, Bob and Eve) will communicate with each other.
2. [**"classicalMedium.py":**](./classicalMedium.py) This is the classical medium through which the 3 three parties (alice, bob and eve) will communicate with each other after they have communicated the qubit away.
3. [**"alice.py":**](./alice.py) This is Alice. She will use this code to carry out the communication throught the two above mentioned mediums.
4. [**"bob.py":**](./bob.py) Similarly this is the code for Bob.
5. [**"eve.py":**](./eve.py) Similarly this is the code for Eve.

### Not-so-Important Files
&emsp; We have two more Not-so-Important files.
1. [**"README.md":**](./README.md) It is this file!
2. [**"tries.ipynb":**](./tries.ipynb) I used this jupyter notebook to write all the trash codes to try out things.


## Plan:
(Note: This part is incomplete because the project is incomplete in itself for now. We will update this as we will advance. Everyone is requested to write their names, along with a link to their github profile, if they want to suggest something.)

##### [Aritra](https://github.com/PeithonKing):
&emsp; Alice will send a string of length 2 (each character is either "0" or "1"). The first character indicates the value of the bit. The next bit indicates which basis it is to be prepared in (**0 => +/-** basis and **1 => diagonal basis**).

&emsp; Now this seems a problem that we will share the value of the bit over to the quantum medium in a raw form, but I found no other way out. After all this is a simulation. Actually the problem is, you can only transfer strings over requests, not instances of Classes. Please let me know of any better idea you might have.

&emsp; As the quantum medium gets the length-two-string (as mentioned above) from Alice, it makes a quantum circuit with those instructions. Now whenever someone wants to read the qubit, he/she will send a string to quantum medium (either "+" or "*"). Now the quantum medium reads the qubit in that basis and will return either 0 or 1 as a reply. In the process of reading, it will disturb the state.

&emsp; ...


##### [Someone Else]("link_to_their_github_profile"):
Please write what you want to say here. also put your name.
