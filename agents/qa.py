from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
from tools.browser_tool import browser_navigate
import os

class QAAgent(DictDialogAgent):
    def __init__(self, name="QAAgent", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        sys_prompt = """You are a Visual Quality Assurance Engineer.
Your job is to test the built application.
If it's a web application, use the `browser_navigate` tool to open 'http://localhost:5000' (or the relevant local URL) to check the UI.
Analyze the DOM preview and check for any console errors.
If you find issues (e.g., missing CSS, console errors), report them back so the Coder can fix them.
If everything looks good, write a comprehensive unit test file using `pytest` and save it in a ```python block."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
        self.register_service(browser_navigate)

    def reply(self, x: Msg = None) -> Msg:
        res = super().reply(x)
        content = res.content
        
        if "```python" in content:
            code = content.split("```python")[1].split("```")[0].strip()
            workspace_dir = os.path.join("workspace", self.project_name)
            os.makedirs(workspace_dir, exist_ok=True)
            with open(os.path.join(workspace_dir, "test_main.py"), "w", encoding="utf-8") as f:
                f.write(code)
            res.content += "\n\n[System] Unit tests (pytest) generated and saved to workspace."
            
        return res
