"""Old version of the Pledge test script, uses addresses and that is why it did not work (Host in Fundraiser used to 
be classic address of wallet instead of Wallet object"""
from csv import reader

import xrpl
from models.fundraiser import Fundraiser
from models.level import Level
from xrpl.account import get_account_info
from xrpl.clients import JsonRpcClient
testnet_url = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(testnet_url)

addies = []
with open("addresses.csv", "r") as f:
    rows = reader(f, delimiter='\n')
    for row in rows:
        addies.append(row[0])
    # print(f"Addies be like {addies}")

host = addies.pop(0)

fundraiser = Fundraiser("Sandwich Fund", 20000000, [Level(0, 10000, "Friends"), Level(1, 100000, "Bigbois")], host)

print(fundraiser)

host_response = get_account_info(host, client)
print(f"Balance: {host_response.result['account_data']['Balance']}")

patient_zero = xrpl.wallet.Wallet(seed = "joey", sequence = 1)
# pz_response = get_account_info(patient_zero, client)
# print(f"First_pledge balance: {pz_response.result['account_data']['Balance']}")



# fundraiser.pledge(addies[0], 2000)

# host_response = get_account_info(host, client)
# print(f"Balance: {host_response.result['account_data']['Balance']}")

