"""Fundraiser instance."""
from models.level import Level
from xrpl.clients import JsonRpcClient
from xrpl.models.transactions.payment import Payment
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission, XRPLReliableSubmissionException
from xrpl.utils import drops_to_xrp
class Fundraiser():
    def __init__(
            self,
            name: str,
            goal: int,
            levels: Level,
            host: str) -> None:
        self.name = name
        self.goal = goal
        self.drops_raised = 0
        self.levels = levels
        self.host = host
    
    def pledge(
            self,
            sender: str,
            amt: int):
            
        testnet_url = "https://s.altnet.rippletest.net:51234"
        client = JsonRpcClient(testnet_url)

        pledge = Payment(
                    account=sender,
                    amount=amt,
                    destination=self.host,
                 )
        signed_tx = safe_sign_and_autofill_transaction(
            pledge, sender, client)

        tx_id = signed_tx.get_hash()

        try:
            tx_response = send_reliable_submission(signed_tx, client)
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
            self.drops_raised += metadata["delivered_amount"]

        

    def __repr__(self) -> str:
        return f"Fundraiser {self.name}\n\thost:\t{self.host}\n\tprogress:\t{self.drops_raised}/{self.goal}"
