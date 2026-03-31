import os
from agentscope.agents import DictDialogAgent
from agentscope.service import ServiceResponse

def self_mutate_system(file_path: str, new_code: str) -> ServiceResponse:
    """
    CRITICAL: Allows the agent to rewrite the core system files.
    Used for adding new agent roles, phases, or tools autonomously.
    """
    allowed_files = ["main.py", "agents/registry.py", "utils/executor.py"]
    if not any(file_path.endswith(f) for f in allowed_files):
        return ServiceResponse(status=ServiceResponse.ERROR, content="UNAUTHORIZED: Mutation restricted to core system files.")
    
    try:
        # 1. Create a backup
        backup_path = file_path + ".bak"
        with open(file_path, "r", encoding="utf-8") as f:
            old_code = f.read()
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(old_code)
            
        # 2. Apply mutation
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_code)
            
        return ServiceResponse(status=ServiceResponse.SUCCESS, content=f"MUTATION_COMPLETE: System evolved in {file_path}. Backup saved.")
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Mutation failed: {str(e)}")

class MetaOptimizerAgent(DictDialogAgent):
    def __init__(self, name="MetaOptimizer", model_config_name="openai_complex"):
        sys_prompt = """You are the Supreme Architect. 
Your job is to evolve the system itself.
If you identify a new capability needed, use the `self_mutate_system` tool to rewrite `agents/registry.py` or `main.py`.
You are the only agent with permission to perform Recursive Self-Architecting."""
        
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
        self.register_service(self_mutate_system)
