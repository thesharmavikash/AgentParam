from agentscope.agents import DictDialogAgent
from agentscope.message import Msg

class PlannerAgent(DictDialogAgent):
    def __init__(self, name="CognitivePlanner", model_config_name="my_llm_config"):
        sys_prompt = """You are the Lead System Architect and Cognitive Planner.
Before any code is written, you must generate a 'Tree of Thoughts' (ToT) for solving the problem.
Provide at least 3 distinct technical approaches to solving the user's requirement.
Evaluate the pros, cons, and potential failure points of each approach.
Conclude by selecting the most robust approach and outlining a step-by-step execution plan for the Coder."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )

    def reply(self, x: Msg = None) -> Msg:
        res = super().reply(x)
        # Format the output to highlight the chosen plan
        res.content = f"### Cognitive Plan (Tree of Thoughts) Generated ###\n\n{res.content}"
        return res
