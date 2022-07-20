file_cont = "# Codes\n"

files = ['quantumMedium.py', 'classicalMedium.py', "module.py", 'alice.py', 'bob.py', 'eve.py']

for file in files:
    file_cont += f"\n### {file}\n```python\n"
    with open(file) as f:
        f = f.read()
    # f = list(f)
    # c = 0
    # for i in range(len(f)):
    #     c += 1
    #     if f[i] == '\n':
    #         c = 0
    #     elif c == 90:
    #         f.insert(i, '\n')
    #         c = 0
    # file_cont += ''.join(f)
    file_cont += f
    file_cont += "\n```\n"

with open("code_E91.md", "w") as f:
    f.write(file_cont)