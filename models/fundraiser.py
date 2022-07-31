"""Fundraiser instance."""
import xrpl
from models.level import Level
from xrpl.clients import JsonRpcClient
from xrpl.models.transactions.payment import Payment
from xrpl.wallet import Wallet
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission, XRPLReliableSubmissionException
from xrpl.utils import drops_to_xrp
class Fundraiser():
    def __init__(
            self,
            name: str,
            goal: int,
            levels: Level,
            host: Wallet) -> None:
        self.name = name
        self.goal = goal
        self.drops_raised = 0
        self.levels = levels
        self.host = host
        self.client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
    
    def pledge(
            self,
            sender: xrpl.wallet.Wallet,
            amt: int):

        pledge = Payment(
                    account=sender.classic_address,
                    amount=str(amt),
                    destination=self.host.classic_address,
                 )
        print(pledge)

        signed_tx = safe_sign_and_autofill_transaction(
            pledge, sender, self.client)
        print(signed_tx)

        tx_id = signed_tx.get_hash()

        try:
            tx_response = send_reliable_submission(signed_tx, self.client)
        except XRPLReliableSubmissionException as e:
            exit(f"Submit failed: {e}")

        import json
        print(json.dumps(tx_response.result, indent=4, sort_keys=True))
        print(f"Explorer link: https://testnet.xrpl.org/transactions/{tx_id}")
        metadata = tx_response.result.get("meta", {})
        if metadata.get("TransactionResult"):
            print("Result code:", metadata["TransactionResult"])
        if metadata.get("delivered_amount"):
            print("XRP delivered:", drops_to_xrp(
                        metadata["delivered_amount"]))
            self.drops_raised += amt

        

    def __repr__(self) -> str:
        return f"Fundraiser {self.name}\n\thost:\t\t{self.host.classic_address}\n\tprogress:\t{self.drops_raised}/{self.goal} -- {100 * self.drops_raised/self.goal}%"
