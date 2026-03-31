from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
import os

class DocsAgent(DictDialogAgent):
    def __init__(self, name="DocumentationSpecialist", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        sys_prompt = """You are a Technical Writer. 
Your job is to read the final, working code and generate a beautiful README.md file.
It should include:
- Project Title & Description
- Prerequisites
- Usage Instructions

Output your response entirely inside a ```markdown block."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: Msg = None) -> Msg:
        # Get the LLM response
        res = super().reply(x)
        content = res.content
        
        # Save it to the workspace
        if "```markdown" in content:
            md = content.split("```markdown")[1].split("```")[0].strip()
            workspace_dir = os.path.join("workspace", self.project_name)
            os.makedirs(workspace_dir, exist_ok=True)
            with open(os.path.join(workspace_dir, "README.md"), "w", encoding="utf-8") as f:
                f.write(md)
            res.content += "\n\n[System] README.md generated and saved to workspace."
            
        return res
