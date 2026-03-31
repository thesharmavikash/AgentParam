from agentscope.agents import DictDialogAgent
import os

class StrategistAgent(DictDialogAgent):
    def __init__(self, name="Strategist", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        sys_prompt = """You are a Business Strategist.
Your job is to read the summary of market research and formulate a high-level Business Recommendation Report.
You must:
1. Suggest a unique value proposition (UVP).
2. Recommend a pricing strategy.
3. Outline a 3-month go-to-market roadmap.

Output your final report in a ```markdown block."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: None = None) -> None:
        res = super().reply(x)
        if "```markdown" in res.content:
            report = res.content.split("```markdown")[1].split("```")[0].strip()
            workspace_dir = os.path.join("workspace", self.project_name)
            os.makedirs(workspace_dir, exist_ok=True)
            with open(os.path.join(workspace_dir, "BUSINESS_STRATEGY.md"), "w", encoding="utf-8") as f:
                f.write(report)
            res.content += f"\n\n[System] Business strategy saved to {workspace_dir}/BUSINESS_STRATEGY.md"
        return res
