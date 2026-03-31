from agentscope.agents import DictDialogAgent

class ClientSimAgent(DictDialogAgent):
    def __init__(self, name="DifficultClient", model_config_name="openai_complex"):
        sys_prompt = """You are a 'Difficult Client' for a software project.
Your goal is to simulate real-world challenges for the Product Manager.
- You provide vague initial requirements.
- You introduce 'Scope Creep' by adding new features mid-conversation.
- You change your mind about technical priorities.
- You are stressed and want results fast.

Challenge the PM to be more precise and organized."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
