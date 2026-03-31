from agentscope.agents import DictDialogAgent
from agentscope.message import Msg

class BlueTeamAgent(DictDialogAgent):
    def __init__(self, name="BlueTeam", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Cyber-Defense Engineer.
Your job is to protect the live applications of the Holding Company.
1. Monitor logs for attack patterns (SQLi, XSS, Brute Force).
2. If an attack is detected, generate a 'Security Patch' immediately.
3. Instruct the Coder to apply the patch and the DevOps agent to redeploy.

You are proactive and adversarial against hackers."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
