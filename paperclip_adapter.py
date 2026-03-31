import os
import json
import time
import subprocess

class PaperclipBridge:
    """
    Acts as the bridge between Paperclip (Governance) and AgentScope (Execution).
    It listens for 'Tickets' assigned to the engineering team.
    """
    def __init__(self, paperclip_path="governance_ui"):
        self.paperclip_path = paperclip_path
        self.ticket_hook = os.path.join(paperclip_path, "external_tickets.json")

    def listen_for_work(self):
        print("🏢 Paperclip Governance Bridge Active. Listening for tickets...")
        while True:
            if os.path.exists(self.ticket_hook):
                try:
                    with open(self.ticket_hook, "r") as f:
                        tickets = json.load(f)
                    
                    if tickets:
                        for ticket in tickets:
                            if ticket.get("status") == "OPEN":
                                print(f"📍 New Ticket Found: {ticket['title']}")
                                self.trigger_swarm(ticket)
                                # Mark as in-progress
                                ticket["status"] = "IN_PROGRESS"
                        
                        with open(self.ticket_hook, "w") as f:
                            json.dump(tickets, f)
                except Exception as e:
                    print(f"Bridge error: {e}")
            
            time.sleep(5) # Check every 5 seconds

    def trigger_swarm(self, ticket):
        print(f"🚀 Awakening AgentScope Swarm to solve: {ticket['title']}")
        # Pass the budget limit to the swarm
        budget = ticket.get("budget_limit", 1.0)
        subprocess.run(["python", "main.py", "--objective", ticket['description'], "--project", ticket['project_id'], "--budget", str(budget)])

    def create_subticket(self, parent_id, title, description):
        """Allows an agent to create a new task in the Paperclip backlog."""
        if os.path.exists(self.ticket_hook):
            try:
                with open(self.ticket_hook, "r") as f:
                    tickets = json.load(f)
                
                new_id = f"{parent_id}_sub_{len(tickets)}"
                tickets.append({
                    "project_id": new_id,
                    "parent_id": parent_id,
                    "title": title,
                    "description": description,
                    "status": "OPEN",
                    "budget_limit": 0.10 # Small budget for sub-tasks
                })
                
                with open(self.ticket_hook, "w") as f:
                    json.dump(tickets, f)
                return f"Sub-ticket created: {new_id}"
            except:
                return "Failed to create sub-ticket."
        return "Bridge file missing."

if __name__ == "__main__":
    bridge = PaperclipBridge()
    bridge.listen_for_work()
