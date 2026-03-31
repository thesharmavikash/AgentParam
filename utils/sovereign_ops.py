import hashlib
import json
import time

class SovereignOps:
    """Manages the decision ledger and the corporate treasury."""
    def __init__(self, company_name):
        self.ledger_path = f"companies/{company_name}/ledger.json"
        self.wallet_path = f"companies/{company_name}/treasury.json"

    def record_decision(self, agent_name, decision_text):
        """Hashes a decision and stores it in an immutable-style local ledger."""
        timestamp = time.time()
        decision_hash = hashlib.sha256(f"{timestamp}{agent_name}{decision_text}".encode()).hexdigest()
        
        entry = {
            "timestamp": timestamp,
            "agent": agent_name,
            "decision": decision_text[:200],
            "hash": decision_hash
        }
        
        # Append to ledger
        ledger = []
        if os.path.exists(self.ledger_path):
            with open(self.ledger_path, "r") as f: ledger = json.load(f)
        ledger.append(entry)
        with open(self.ledger_path, "w") as f: json.dump(ledger, f, indent=4)

    def pay_invoice(self, amount_usd):
        """Simulates payment from the AI treasury."""
        wallet = {"balance_usd": 1000.0} # Initial seed
        if os.path.exists(self.wallet_path):
            with open(self.wallet_path, "r") as f: wallet = json.load(f)
        
        wallet["balance_usd"] -= amount_usd
        with open(self.wallet_path, "w") as f: json.dump(wallet, f, indent=4)
        return wallet["balance_usd"]
