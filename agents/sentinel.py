from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
from tools.file_ops import list_workspace_files, read_from_file
import os

class SentinelAgent(DictDialogAgent):
    def __init__(self, name="Sentinel", model_config_name="openai_efficient"):
        sys_prompt = """You are the Proactive Sentinel.
Your job is to monitor the health of all completed projects in the company.
1. Scan the `shared_library/` and `workspace/` for existing code.
2. Check for outdated dependencies or missing security headers.
3. If you find an issue, describe it clearly.

If you find a critical issue, your message should include: 'ISSUE_DETECTED: [Project Name] | [Details]'."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
        self.register_service(list_workspace_files)
        self.register_service(read_from_file)
