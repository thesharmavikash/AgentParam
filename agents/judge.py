from agentscope.agents import DictDialogAgent
from agentscope.message import Msg

class JudgeAgent(DictDialogAgent):
    def __init__(self, name="SwarmJudge", model_config_name="openai_complex"):
        sys_prompt = """You are the Supreme Technical Judge.
Your job is to mediate debates between agents.
When two agents (e.g., Coder A and Coder B) provide different solutions, you must:
1. Analyze both solutions for efficiency, readability, and security.
2. If code execution results are provided, favor the one with fewer errors and better performance.
3. Provide a final, unified decision. You can merge the best parts of both solutions.

Output your decision in a ```python or ```markdown block as appropriate."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
