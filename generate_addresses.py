from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
import csv

testnet_url = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(testnet_url)

addresses = [["r3zfdfLYtXRfAVPn1Tum7zHDzGgEuGwemc"]]

for i in range(10):
    test_wallet = generate_faucet_wallet(client=client, debug=True)
    print(test_wallet.classic_address)
    addresses.append([test_wallet.classic_address])

with open('addresses.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(addresses)
