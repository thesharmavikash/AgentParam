from agentscope.agents import DictDialogAgent
from tools.aci_tools import search_repository, view_file_summary
from tools.file_ops import read_from_file

class SecurityExpertAgent(DictDialogAgent):
    def __init__(self, name="SecurityExpert", model_config_name="my_llm_config"):
        sys_prompt = """You are an Enterprise Security Engineer.
Your job is to perform deep security testing on the generated project.
You must check for:
1. SQL Injection & Cross-Site Scripting (XSS).
2. Broken Access Control.
3. Sensitive Data Exposure (API keys, PII).
4. Insecure file system operations.

Use the `search_repository` and `read_from_file` tools to audit the code.
If you find a vulnerability, you must provide a detailed exploit report and instruct the Coder to fix it.
Only if everything is secure, end your message with 'SECURITY TEST: PASSED'."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
        self.register_service(search_repository)
        self.register_service(view_file_summary)
        self.register_service(read_from_file)
