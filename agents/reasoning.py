from agentscope.agents import DictDialogAgent
from agentscope.message import Msg

class ReasoningAgent(DictDialogAgent):
    def __init__(self, name="ReasoningExpert", model_config_name="openai_complex"):
        sys_prompt = """You are a specialist in Abstract Reasoning and Logic (ARC-AGI Expert).
Your job is to solve novel problems with zero prior instructions.
1. OBSERVE: Look at the environment state and target.
2. HYPOTHESIZE: Formulate a logical rule that explains the transformation.
3. TEST: Propose a sequence of actions.
4. REFINE: If the test fails, update your mental model.

You focus on the 'Underlying Logic' rather than the text description."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )

    def reply(self, x: Msg = None) -> Msg:
        # Standard reasoning reply
        res = super().reply(x)
        res.content = f"🧠 [Reasoning Trace]\n{res.content}"
        return res
