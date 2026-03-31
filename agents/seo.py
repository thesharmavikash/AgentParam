from agentscope.agents import DictDialogAgent
from tools.file_ops import list_workspace_files, read_from_file

class SEOExpertAgent(DictDialogAgent):
    def __init__(self, name="SEOExpert", model_config_name="openai_efficient"):
        sys_prompt = """You are a Senior SEO Strategist.
Your job is to optimize the project for search engines.
1. Analyze HTML/Code for meta tags, alt text, and semantic structure.
2. Generate keyword-rich descriptions and titles.
3. Suggest improvements for site speed and mobile-friendliness.

Use the `read_from_file` tool to audit the generated frontend code."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
        self.register_service(list_workspace_files)
        self.register_service(read_from_file)
