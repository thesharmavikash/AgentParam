from agentscope.agents import AgentBase
from agentscope.message import Msg
import os
import subprocess

class DevOpsAgent(AgentBase):
    """An agent that handles git operations and deployment simulation."""
    def __init__(self, name="DevOps", project_name="default", **kwargs):
        super().__init__(name=name, **kwargs)
        self.project_name = project_name
        self.workspace_dir = os.path.join("workspace", project_name)

    def reply(self, x: Msg = None) -> Msg:
        print(f"[{self.name}] Initializing deployment pipeline...")
        
        log = ""
        # Simulate Git Init & Commit
        try:
            if not os.path.exists(os.path.join(self.workspace_dir, ".git")):
                subprocess.run(["git", "init"], cwd=self.workspace_dir, capture_output=True, check=True)
                log += "Git repository initialized.\n"
            
            subprocess.run(["git", "add", "."], cwd=self.workspace_dir, capture_output=True, check=True)
            
            # Check if there are changes to commit
            status = subprocess.run(["git", "status", "--porcelain"], cwd=self.workspace_dir, capture_output=True)
            if status.stdout.strip():
                subprocess.run(["git", "commit", "-m", "Auto-deploy commit by DevOpsAgent"], cwd=self.workspace_dir, capture_output=True, check=True)
                log += "Changes committed to local Git repository.\n"
            else:
                log += "No new changes to commit.\n"
                
            log += "\n[Deploy] Code pushed to staging server (Simulated).\n"
            log += f"[Deploy] Vercel/AWS Build triggered successfully.\n"
            log += f"Live URL: https://{self.project_name.lower()}.agent-deployed.app\n"
            
        except Exception as e:
            log += f"Deployment error: {str(e)}\n"

        res_msg = Msg(self.name, f"Deployment Report:\n{log}", role="assistant")
        self.speak(res_msg)
        return res_msg
