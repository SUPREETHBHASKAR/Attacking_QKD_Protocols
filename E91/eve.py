from module import *

name = "eve"
print(f"Hi! This is {name.title()}!")
baseOpt = ['W', 'Z']

singlets_sent = int(requests.get(quantuMedium).text)
send_bases(baseOpt, singlets_sent, name)
print("completed eavesdropping!")