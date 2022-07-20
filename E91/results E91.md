# Code Results

## When Eve does not intercepts:

**"quantumMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\quantumMedium.py
 * Serving Flask app 'quantumMedium' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5001/ (Press CTRL+C to quit)

someone asked for the number of singlets... returned 2000
127.0.0.1 - - [19/Jul/2022 10:30:08] "GET / HTTP/1.1" 200 -

Alice sent choice of bases
127.0.0.1 - - [19/Jul/2022 10:30:10] "POST /send_bases HTTP/1.1" 200 -

someone asked for the number of singlets... returned 2000
127.0.0.1 - - [19/Jul/2022 10:30:10] "GET / HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:30:12] "POST /measure_qubits HTTP/1.1" 200 -

Bob sent choice of bases

As the Quantum Medium has both the bases of Alice and Bob, it can start making measurements...

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:30:24] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:30:36] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:31:03] "POST /measure_qubits HTTP/1.1" 200 -

measurements completed!
127.0.0.1 - - [19/Jul/2022 10:31:03] "POST /send_bases HTTP/1.1" 200 -

Bob is requesting for the measurements. Measurements are now ready, so Quantum Medium is  returning the results.
127.0.0.1 - - [19/Jul/2022 10:31:05] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. Measurements are now ready, so Quantum Medium is  returning the results.
127.0.0.1 - - [19/Jul/2022 10:31:15] "POST /measure_qubits HTTP/1.1" 200 -
```

**"classicalMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\classicalMedium.py
 * Serving Flask app 'classicalMedium' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:31:07] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:31:10] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:31:13] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:31:16] "POST /get_alice_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. The Classical Medium already has Bob's bases, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:31:17] "POST /get_bob_bases HTTP/1.1" 200 -

Alice sent her unused Bits and is requesting for Bob's unused Bits. But Bob hasn't sent his unused Bits yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:31:19] "POST /get_bob_uBits HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. The Classical Medium already has Alice's bases, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:31:19] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his unused Bits and is requesting for Alice's unused Bits. The Classical Medium already has Alice's unused Bits, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:31:21] "POST /get_alice_uBits HTTP/1.1" 200 -

Alice sent her unused Bits and is requesting for Bob's unused Bits. The Classical Medium already has Bob's unused Bits, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:31:22] "POST /get_bob_uBits HTTP/1.1" 200 -
```

**"alice.py":** 

```
Hi! This is Alice!
Sending bases...
Reading qubits...
Reading qubits...
Reading qubits...
Reading qubits...
Reading qubits...
chsh score: -2.831877117951897
0010000011010101111100001001101000100101000001100001000000000001010001011010001011101000011010000100100110001100100010100010011011101100101000100011010001001000101100100111110011100011111010010110101001011101110001011111101000111100010110010100110101011101111000010110011001000101010000001000111010010001110111000100100011000101010001101000110110101000001011000010011010110011011000100101001001100111110010111010110101101101101010101101
```

**"bob.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\bob.py
Hi! This is Bob!
Sending bases...
Reading qubits...
chsh score: -2.831877117951897
0010000011010101111100001001101000100101000001100001000000000001010001011010001011101000011010000100100110001100100010100010011011101100101000100011010001001000101100100111110011100011111010010110101001011101110001011111101000111100010110010100110101011101111000010110011001000101010000001000111010010001110111000100100011000101010001101000110110101000001011000010011010110011011000100101001001100111110010111010110101101101101010101101
```

## When Eve intercepts:
**"quantumMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\quantumMedium.py
 * Serving Flask app 'quantumMedium' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5001/ (Press CTRL+C to quit)

someone asked for the number of singlets... returned 2000
127.0.0.1 - - [19/Jul/2022 10:35:08] "GET / HTTP/1.1" 200 -

Eve sent choice of bases
127.0.0.1 - - [19/Jul/2022 10:35:10] "POST /send_bases HTTP/1.1" 200 -

someone asked for the number of singlets... returned 2000
127.0.0.1 - - [19/Jul/2022 10:35:34] "GET / HTTP/1.1" 200 -

someone asked for the number of singlets... returned 2000
127.0.0.1 - - [19/Jul/2022 10:35:34] "GET / HTTP/1.1" 200 -

Alice sent choice of bases
127.0.0.1 - - [19/Jul/2022 10:35:36] "POST /send_bases HTTP/1.1" 200 -

Bob sent choice of bases

As the Quantum Medium has both the bases of Alice and Bob, it can start making measurements...

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:35:38] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:35:50] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:36:02] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. But measurements are not ready yet, so Quantum Medium requests him/her to wait a bit before asking again!
127.0.0.1 - - [19/Jul/2022 10:36:28] "POST /measure_qubits HTTP/1.1" 200 -

measurements completed!
127.0.0.1 - - [19/Jul/2022 10:36:28] "POST /send_bases HTTP/1.1" 200 -

Bob is requesting for the measurements. Measurements are now ready, so Quantum Medium is  returning the results.
127.0.0.1 - - [19/Jul/2022 10:36:30] "POST /measure_qubits HTTP/1.1" 200 -

Alice is requesting for the measurements. Measurements are now ready, so Quantum Medium is  returning the results.
127.0.0.1 - - [19/Jul/2022 10:36:40] "POST /measure_qubits HTTP/1.1" 200 -
```

**"classicalMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\classicalMedium.py
 * Serving Flask app 'classicalMedium' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:36:32] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:36:35] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:36:39] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. But Alice hasn't sent her bases yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:36:42] "POST /get_alice_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. The Classical Medium already has Bob's bases, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:36:42] "POST /get_bob_bases HTTP/1.1" 200 -

Alice sent her unused Bits and is requesting for Bob's unused Bits. But Bob hasn't sent his unused Bits yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:36:44] "POST /get_bob_uBits HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. The Classical Medium already has Alice's bases, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:36:45] "POST /get_alice_bases HTTP/1.1" 200 -

Bob sent his unused Bits and is requesting for Alice's unused Bits. The Classical Medium already has Alice's unused Bits, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:36:47] "POST /get_alice_uBits HTTP/1.1" 200 -

Alice sent her unused Bits and is requesting for Bob's unused Bits. The Classical Medium already has Bob's unused Bits, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:36:48] "POST /get_bob_uBits HTTP/1.1" 200 -
```

**"eve.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\eve.py
Hi! This is Eve!
Sending bases...
completed eavesdropping!

```

**"alice.py":** 

```
PS C:\Users\amukh\Desktop\QKD\E91> python .\alice.py
Hi! This is Alice!
Sending bases...
Reading qubits...
Reading qubits...
Reading qubits...
Reading qubits...
Reading qubits...
chsh score: -1.9656904472046612
Eve is here! Abort!
```

**"bob.py":** 

```
Hi! This is Bob!
Sending bases...
Reading qubits...
chsh score: -1.9656904472046612
Eve is here! Abort!
```
