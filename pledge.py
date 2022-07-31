import xrpl
import logging
from models.fundraiser import Fundraiser
from models.level import Level
import utils.generate_wallets as gw

logging.basicConfig(filename="logs/pledge.log", filemode='w', level=logging.INFO)
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = xrpl.clients.JsonRpcClient(JSON_RPC_URL)

wallets = gw.generate_wallets()

host = wallets.pop()

first_supporter = wallets.pop()

host_info = xrpl.models.AccountInfo(account=host.classic_address, ledger_index="validated", strict=True)
host_response = client.request(host_info)
first_supporter_info = xrpl.models.AccountInfo(account=first_supporter.classic_address, ledger_index="validated", strict=True)
first_supporter_response = client.request(first_supporter_info)

logging.info(f"Status: {host_response.status}")
logging.info(f"Host starting balance: {host_response.result['account_data']['Balance']}")
logging.info(f"Status: {first_supporter_response.status}")
logging.info(f"Supporter starting balance: {first_supporter_response.result['account_data']['Balance']}")

fundraiser = Fundraiser("Sandwich Fund", 20000000, [Level(0, 10000, "Friends"), Level(1, 100000, "Bigbois")], host)

logging.info(f"{fundraiser}")

fundraiser.pledge(first_supporter, 2000000)

host_info = xrpl.models.AccountInfo(account=host.classic_address, ledger_index="validated", strict=True)
host_response = client.request(host_info)
first_supporter_info = xrpl.models.AccountInfo(account=first_supporter.classic_address, ledger_index="validated", strict=True)
first_supporter_response = client.request(first_supporter_info)
logging.info(f"Status: {host_response.status}")
logging.info(f"Host ending balance: {host_response.result['account_data']['Balance']}")
logging.info(f"Status: {first_supporter_response.status}")
logging.info(f"Supporter ending balance: {first_supporter_response.result['account_data']['Balance']}")
logging.info(f"{fundraiser}")
