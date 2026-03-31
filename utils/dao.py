import json
import os

class DAOGovernance:
    """Simulates a Decentralized Board where agents vote on technical proposals."""
    def __init__(self, company_name):
        self.proposal_path = f"companies/{company_name}/proposals.json"

    def submit_proposal(self, proposer, title, description):
        proposals = []
        if os.path.exists(self.proposal_path):
            with open(self.proposal_path, "r") as f: proposals = json.load(f)
        
        new_proposal = {
            "id": len(proposals),
            "proposer": proposer,
            "title": title,
            "description": description,
            "votes": {},
            "status": "VOTING"
        }
        proposals.append(new_proposal)
        with open(self.proposal_path, "w") as f: json.dump(proposals, f, indent=4)
        return new_proposal["id"]

    def cast_vote(self, proposal_id, agent_name, vote, trust_score):
        """Vote weight is determined by the agent's Trust Score."""
        with open(self.proposal_path, "r") as f: proposals = json.load(f)
        
        for p in proposals:
            if p["id"] == proposal_id:
                p["votes"][agent_name] = {"vote": vote, "weight": trust_score}
                
                # Check for consensus
                total_weight = sum(v["weight"] for v in p["votes"].values())
                yes_weight = sum(v["weight"] for v in p["votes"].values() if v["vote"] == "YES")
                
                if yes_weight > (total_weight / 2) and len(p["votes"]) >= 3:
                    p["status"] = "PASSED"
                elif (total_weight - yes_weight) > (total_weight / 2) and len(p["votes"]) >= 3:
                    p["status"] = "REJECTED"
        
        with open(self.proposal_path, "w") as f: json.dump(proposals, f, indent=4)
        return proposals[proposal_id]["status"]
