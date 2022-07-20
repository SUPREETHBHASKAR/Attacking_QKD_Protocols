# Code Results

## When Eve does not intercept:

**"quantumMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\quantumMedium.py
 * Serving Flask app 'quantumMedium' (lazy loading)
 * Environment: production
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5050/ (Press CTRL+C to quit)
someone asks for the key-length, Quantum Medium return 2500
127.0.0.1 - - [19/Jul/2022 10:07:55] "GET / HTTP/1.1" 200 -
someone asks for the key-length, Quantum Medium return 2500
127.0.0.1 - - [19/Jul/2022 10:07:55] "GET / HTTP/1.1" 200 -

Alice sends all the 2500 qubit
100%|████████████████████████████████| 2500/2500 [00:00<00:00, 8338.95it/s]
127.0.0.1 - - [19/Jul/2022 10:07:57] "POST /send_qubit HTTP/1.1" 200 -

Someone measures the qubits in his/her choice of bases.
100%|█████████████████████████████████| 2500/2500 [00:21<00:00, 116.72it/s]
127.0.0.1 - - [19/Jul/2022 10:08:19] "POST /read_qubits HTTP/1.1" 200 -
```

**"classicalMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\classicalMedium.py
 * Serving Flask app 'classicalMedium' (lazy loading)
 * Environment: production
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

Alice sent her bases and is requesting for Bob's bases. But Bob hasn't sent his bases yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:07:59] "POST /get_bob_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. The Classical Medium already has Alice's bases, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:08:21] "POST /get_alice_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. The Classical Medium already has Bob's bases, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:08:22] "POST /get_bob_bases HTTP/1.1" 200 -

Bob is requesting for Alice's sample. But Alice hasn't sent her sample yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:08:23] "GET /get_sample HTTP/1.1" 200 -

Alice sent her sample.
127.0.0.1 - - [19/Jul/2022 10:08:24] "POST /send_sample HTTP/1.1" 200 -

Bob is requesting for Alice's sample. The Classical Medium already has Alice's sample, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:08:26] "GET /get_sample HTTP/1.1" 200 -

Alice is requesting for Bob's decision on whether to proceed with the key or start the process of resending another key.
But Bob hasn't sent his decision yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:08:26] "GET /status HTTP/1.1" 200 -

Bob is sending his decision on whether to proceed with the key or start the process of resending another key.
127.0.0.1 - - [19/Jul/2022 10:08:28] "POST /status HTTP/1.1" 200 -

Alice is requesting for Bob's decision on whether to proceed with the key or start the process of resending another key.
The Classical Medium already has Bob's decision, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:08:33] "GET /status HTTP/1.1" 200 -
```

**"alice.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\bob.py
Hi! This is Bob!
match = 100.0%
Success
key length = 929
key = 01000110101101111111001011101101000111100010010101000011010110011101111111111010000000101110101010011100010101011100110010111110000100110011010010110111100000100111000111110010011011111001001110110001011001010010011110010010111011101101110100011100110101101111101000010011011010011010001000110000101000110110111000111011100111101000001101110000000101001110100001001100111111011101000111100100111111101110110110000001101010010110111101011011010010001000000010110100100000011000110101100010100001001100101100011000001101010100110101110101010111100100001001101001110001111111111110011111101011110110111101010011111111111011101111101001001011011011001100111001110011110010100011010010011110000111111111100101101100000010010110101111101000110011000000110110000001111001101100010111001001010111111100011101110111011011111110010000110111001100011100011100100001110110110010110000000100110101011111011100000000100111010111001111100001101
```

**"bob.py":** 

```
Hi! This is Alice!
sample length = 375
key = 01000110101101111111001011101101000111100010010101000011010110011101111111111010000000101110101010011100010101011100110010111110000100110011010010110111100000100111000111110010011011111001001110110001011001010010011110010010111011101101110100011100110101101111101000010011011010011010001000110000101000110110111000111011100111101000001101110000000101001110100001001100111111011101000111100100111111101110110110000001101010010110111101011011010010001000000010110100100000011000110101100010100001001100101100011000001101010100110101110101010111100100001001101001110001111111111110011111101011110110111101010011111111111011101111101001001011011011001100111001110011110010100011010010011110000111111111100101101100000010010110101111101000110011000000110110000001111001101100010111001001010111111100011101110111011011111110010000110111001100011100011100100001110110110010110000000100110101011111011100000000100111010111001111100001101
```

## When Eve intercepts:
**"quantumMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\quantumMedium.py
 * Serving Flask app 'quantumMedium' (lazy loading)
 * Environment: production
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5050/ (Press CTRL+C to quit)
someone asks for the key-length, Quantum Medium return 2500
127.0.0.1 - - [19/Jul/2022 10:02:23] "GET / HTTP/1.1" 200 -

Alice sends all the 2500 qubit
100%|████████████████████████████████| 2500/2500 [00:00<00:00, 7175.33it/s]
127.0.0.1 - - [19/Jul/2022 10:02:26] "POST /send_qubit HTTP/1.1" 200 -
someone asks for the key-length, Quantum Medium return 2500
127.0.0.1 - - [19/Jul/2022 10:02:31] "GET / HTTP/1.1" 200 -

Someone measures the qubits in his/her choice of bases.
100%|█████████████████████████████████| 2500/2500 [00:24<00:00, 101.28it/s]
127.0.0.1 - - [19/Jul/2022 10:02:58] "POST /read_qubits HTTP/1.1" 200 -
someone asks for the key-length, Quantum Medium return 2500
127.0.0.1 - - [19/Jul/2022 10:03:07] "GET / HTTP/1.1" 200 -

Someone measures the qubits in his/her choice of bases.
100%|█████████████████████████████████| 2500/2500 [00:23<00:00, 104.44it/s]
127.0.0.1 - - [19/Jul/2022 10:03:33] "POST /read_qubits HTTP/1.1" 200 -
```

**"classicalMedium.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\classicalMedium.py
 * Serving Flask app 'classicalMedium' (lazy loading)
 * Environment: production
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-787-847
 * Running on http://localhost:5000/ (Press CTRL+C to quit)

Alice sent her bases and is requesting for Bob's bases. But Bob hasn't sent his bases yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:02:28] "POST /get_bob_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. But Bob hasn't sent his bases yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:02:51] "POST /get_bob_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. But Bob hasn't sent his bases yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:03:13] "POST /get_bob_bases HTTP/1.1" 200 -

Bob sent his bases and is requesting for Alice's bases. The Classical Medium already has Alice's bases, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:03:35] "POST /get_alice_bases HTTP/1.1" 200 -

Alice sent her bases and is requesting for Bob's bases. The Classical Medium already has Bob's bases, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:03:36] "POST /get_bob_bases HTTP/1.1" 200 -

Bob is requesting for Alice's sample. But Alice hasn't sent her sample yet, so he waits.
127.0.0.1 - - [19/Jul/2022 10:03:37] "GET /get_sample HTTP/1.1" 200 -

Alice sent her sample.
127.0.0.1 - - [19/Jul/2022 10:03:38] "POST /send_sample HTTP/1.1" 200 -

Bob is requesting for Alice's sample. The Classical Medium already has Alice's sample, so it gives it to him.
127.0.0.1 - - [19/Jul/2022 10:03:40] "GET /get_sample HTTP/1.1" 200 -

Alice is requesting for Bob's decision on whether to proceed with the key or start the process of resending another key.
But Bob hasn't sent his decision yet, so she waits.
127.0.0.1 - - [19/Jul/2022 10:03:40] "GET /status HTTP/1.1" 200 -

Bob is sending his decision on whether to proceed with the key or start the process of resending another key.
127.0.0.1 - - [19/Jul/2022 10:03:42] "POST /status HTTP/1.1" 200 -

Alice is requesting for Bob's decision on whether to proceed with the key or start the process of resending another key.
The Classical Medium already has Bob's decision, so it gives it to her.
127.0.0.1 - - [19/Jul/2022 10:03:47] "GET /status HTTP/1.1" 200 -
```

**"eve.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\eve.py
Hi! This is Eve!
completed eavesdropping!
```

**"alice.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\alice.py
Hi! This is Alice!
sample length = 375
Eve Detected, mission abort!
```

**"bob.py":** 

```
PS C:\Users\amukh\Desktop\QKD\BB84_1> python .\bob.py
Hi! This is Bob!
match = 59.46666666666667%
Eve Detected, mission abort!
```
