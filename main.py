from csv import reader

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
host = addies.pop(0)

fundraiser = Fundraiser("Sandwich Fund", 20000000, [Level(0, 10000, "Friends"), Level(1, 100000, "Bigbois")], host)

print(fundraiser)

host_response = get_account_info(host, client)
print(f"Balance: {host_response.result['account_data']['Balance']}")

fundraiser.pledge(addies[0], 2000)

host_response = get_account_info(host, client)
print(f"Balance: {host_response.result['account_data']['Balance']}")

