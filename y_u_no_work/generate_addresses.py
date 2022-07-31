from xrpl import XRPLException
from xrpl.clients import JsonRpcClient
import xrpl.wallet as wallet
import csv
from threading import Thread

testnet_url = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(testnet_url)

addresses = []

def generate_bois(ind):
    try:
        test_wallet = wallet.generate_faucet_wallet(client=client, debug=True)
        print(f"Thread {ind}: {test_wallet}")
        addresses.append([test_wallet.classic_address])
    except XRPLException as e:
        print(f"Exception thread {ind}: {e}")

threads = []
for i in range(10):
    threads.append(Thread(target=generate_bois, args=(i,)))
    threads[i].start()

for t in threads:
    t.join()

with open('addresses.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(addresses)

# ! Works as a script, but only stores the classic addresses, figure out how to get the seeds + sequences to store instead
# ! For now, using similar script to just get a list of wallets
