from agentscope.agents import DictDialogAgent
from tools.aci_tools import view_file_summary, search_repository
from tools.file_ops import read_from_file, write_to_file
from agentscope.message import Msg
import os
import subprocess

class GitHubResolverAgent(DictDialogAgent):
    def __init__(self, name="SWE-Agent", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        self.workspace_dir = os.path.join("workspace", project_name)
        
        sys_prompt = f"""You are a State-of-the-Art autonomous software engineer (like SWE-agent or Devin).
Your task is to resolve a GitHub issue autonomously.

Workflow:
1. Use `search_repository` to find where the bug might live.
2. Use `view_file_summary` to understand the file structure without reading the whole thing.
3. Use `read_from_file` to read the specific buggy code.
4. Use `write_to_file` to apply the patch.

You have full control over the `{self.workspace_dir}` directory."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
        
        # Equip with ACI and native tools
        self.register_service(search_repository)
        self.register_service(view_file_summary)
        self.register_service(read_from_file)
        self.register_service(write_to_file)

    def reply(self, x: Msg = None) -> Msg:
        # Pre-hook: If the user provides a repo URL, clone it first.
        content = x.content
        if "github.com" in content and ".git" in content:
            # Extract URL
            import re
            url_match = re.search(r'(https://github\.com/\S+\.git)', content)
            if url_match:
                repo_url = url_match.group(1)
                print(f"[{self.name}] Cloning repository: {repo_url} into {self.workspace_dir}")
                os.makedirs(self.workspace_dir, exist_ok=True)
                try:
                    subprocess.run(["git", "clone", repo_url, "."], cwd=self.workspace_dir, capture_output=True, check=True)
                    x.content += f"\n\n[System Info: Repository cloned successfully to {self.workspace_dir}. Begin ACI analysis.]"
                except Exception as e:
                    x.content += f"\n\n[System Info: Failed to clone repository. Error: {str(e)}]"

        return super().reply(x)
