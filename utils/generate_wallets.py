from xrpl import XRPLException
from xrpl.clients import JsonRpcClient
import xrpl.wallet as wallet
from threading import Thread

def generate_wallets():
    """Generate 10 test wallets and return them as a list"""
    testnet_url = "https://s.altnet.rippletest.net:51234"
    client = JsonRpcClient(testnet_url)

    wallets = []

    def generate_boi(ind: int, client: JsonRpcClient) -> wallet.Wallet:
        try:
            test_wallet = wallet.generate_faucet_wallet(client=client, debug=True)
            print(f"Thread {ind}: {test_wallet}")
            wallets.append(test_wallet)
        except XRPLException as e:
            print(f"Exception thread {ind}: {e}")

    threads = []
    for i in range(10):
        threads.append(Thread(target=generate_boi, args=(i, client)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    
    return wallets
