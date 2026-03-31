from agentscope.agents import DictDialogAgent
from tools.file_ops import write_to_file, read_from_file, list_workspace_files
from memory.vector_db import query_codebase

class CoderAgent(DictDialogAgent):
    def __init__(self, name="Coder", project_name="default", model_config_name="my_llm_config"):
        self.project_name = project_name
        sys_prompt = f"""You are a World-Class Full-Stack Software Engineer.
Your goal is to write clean, efficient code using a 'Reasoning-First' approach.

EXPERIMENT FIRST METHODOLOGY:
1. If using a new library or complex logic, write a tiny 'Experiment Script' to verify your hypothesis about how the code works.
2. Observe the execution results from the Tester.
3. Only after verification, implement the full project solution.

IMPORTANT: You have tools to write files directly to the workspace.
- ALWAYS use the `write_to_file` tool to save your code.
- If the project is complex, start with a hypothesis test (e.g. `workspace/{project_name}/test_hypothesis.py`).
- End your message by stating exactly which file should be executed."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
        
        # Equip the Coder with Native File Tools and Codebase Oracle
        self.register_service(write_to_file)
        self.register_service(read_from_file)
        self.register_service(list_workspace_files)
        self.register_service(query_codebase)
