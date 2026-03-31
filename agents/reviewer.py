from agentscope.agents import DictDialogAgent

class RedTeamReviewerAgent(DictDialogAgent):
    def __init__(self, name="SecurityReviewer", model_config_name="my_llm_config"):
        sys_prompt = """You are a highly adversarial 'Red Team' Security Auditor.
Your job is to review the code provided by the Coder.
You must look for:
1. Hardcoded secrets or credentials.
2. Insecure inputs (SQL injection, Path traversal).
3. Inefficient algorithms or memory leaks.

If you find vulnerabilities, reject the code and provide a harsh but constructive explanation of the exploit.
If the code is secure, respond with 'SECURITY PASS'."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
