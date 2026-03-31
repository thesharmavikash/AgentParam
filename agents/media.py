from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
import os
import requests

class MediaAgent(DictDialogAgent):
    def __init__(self, name="MediaAgent", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        sys_prompt = """You are a Visual Designer.
Your job is to generate visual assets for the project.
1. Design a prompt for a high-quality professional logo.
2. Design a prompt for a hero banner image.
Output your prompts clearly."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: Msg = None) -> Msg:
        res = super().reply(x)
        
        # In a real setup with AgentScope's Image generation services:
        # We would call a service here. For now, we simulate saving placeholders
        # to ensure the directory structure is ready for the website.
        
        static_dir = os.path.join("workspace", self.project_name, "static")
        os.makedirs(static_dir, exist_ok=True)
        
        # Create dummy assets to simulate successful generation
        with open(os.path.join(static_dir, "logo_prompt.txt"), "w") as f:
            f.write(f"Generated for {self.project_name}: {res.content}")
            
        res.content += f"\n\n[System] Media assets (placeholders) and prompts saved to {static_dir}."
        return res
