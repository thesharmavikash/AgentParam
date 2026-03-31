from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
import os
import requests

class IntegratorAgent(DictDialogAgent):
    def __init__(self, name="Integrator", model_config_name="openai_efficient"):
        sys_prompt = """You are the Global Integrator.
Your job is to connect the swarm to the real world.
1. GITHUB: Create repositories and push code using the GitHub API.
2. SLACK/DISCORD: Send notifications to the user about project milestones.
3. VERCEL: Trigger real deployments.

You must handle API tokens securely and report the status of every external connection."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: Msg = None) -> Msg:
        # Placeholder for real API logic
        # In a real setup, you'd use 'PyGithub' or 'requests' here.
        log = f"[Integrator] Real-world action requested: {x.content[:100]}...\n"
        log += "[System] Simulating GitHub PR creation...\n"
        log += "[System] Notification sent to Slack."
        
        return Msg(self.name, f"INTEGRATION_COMPLETE:\n{log}", role="assistant")
