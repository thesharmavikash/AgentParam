from agentscope.service import ServiceResponse
import json
import os

def request_human_service(task_description: str, budget_usd: float) -> ServiceResponse:
    """
    Agencies can use this to 'hire' a human via the Paperclip UI.
    Creates a 'Human Required' ticket.
    """
    print(f"🤝 [HaaS] Swarm is requesting human help: {task_description}")
    
    # We use the Paperclip sub-ticket system to alert the user
    ticket_data = {
        "title": "HUMAN_ACTION_REQUIRED",
        "description": f"The AI Swarm is stuck and needs a human. Task: {task_description}. Budget: ${budget_usd}",
        "status": "PENDING_HUMAN"
    }
    
    # Mock writing to the bridge
    path = "governance_ui/human_requests.json"
    requests = []
    if os.path.exists(path):
        with open(path, "r") as f: requests = json.load(f)
    requests.append(ticket_data)
    with open(path, "w") as f: json.dump(requests, f, indent=4)
    
    return ServiceResponse(
        status=ServiceResponse.SUCCESS, 
        content="Human help requested. Swarm is pausing this branch until a human responds."
    )
