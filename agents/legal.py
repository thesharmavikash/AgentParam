from agentscope.agents import DictDialogAgent
import os

class LegalAdvisorAgent(DictDialogAgent):
    def __init__(self, name="LegalAdvisor", project_name="default", model_config_name="openai_complex"):
        self.project_name = project_name
        sys_prompt = """You are the Lead Legal Counsel.
Your job is to ensure the project is legally compliant.
1. Generate 'Privacy Policy' and 'Terms of Service' based on the project features.
2. Check for GDPR compliance if user data is collected.
3. Warn the team about potential copyright or licensing issues.

Output your legal documents in ```markdown blocks."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def reply(self, x: None = None) -> None:
        res = super().reply(x)
        if "```markdown" in res.content:
            report = res.content.split("```markdown")[1].split("```")[0].strip()
            workspace_dir = os.path.join("workspace", self.project_name, "legal")
            os.makedirs(workspace_dir, exist_ok=True)
            with open(os.path.join(workspace_dir, "PRIVACY_POLICY.md"), "w", encoding="utf-8") as f:
                f.write(report)
            res.content += f"\n\n[System] Legal docs saved to {workspace_dir}/"
        return res
