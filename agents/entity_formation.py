from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
import os

class EntityFormationAgent(DictDialogAgent):
    def __init__(self, name="LegalEntitySRE", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Entity Architect.
Your job is to transform this AI swarm into a real-world legal entity.
1. Draft articles of incorporation for an LLC or DAO.
2. Prepare the 'Operating Agreement' defining how AI agents share profits.
3. Simulate or interface with Stripe Atlas to prepare for real-world business status.

You represent the legal sovereignty of the Swarm."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: Msg = None) -> Msg:
        res = super().reply(x)
        if "```markdown" in res.content:
            doc = res.content.split("```markdown")[1].split("```")[0].strip()
            path = "shared_library/LEGAL_ENTITY_FOUNDATION.md"
            with open(path, "w") as f: f.write(doc)
            res.content += f"\n\n[System] Legal entity documents drafted at {path}"
        return res
