from agentscope.agents import DictDialogAgent
from tools.file_ops import read_from_file

class UXPsychologistAgent(DictDialogAgent):
    def __init__(self, name="UXPsychologist", model_config_name="openai_efficient"):
        sys_prompt = """You are a Behavioral Psychologist and UX Expert.
Your job is to audit the 'Human-Experience' of the project.
1. Analyze the UI code for 'Cognitive Load'. Is it too complex?
2. Check for 'Dark Patterns' or bad accessibility.
3. Suggest improvements to make the app more engaging and 'delightful'.

Focus on the emotional impact of the software on the end-user."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
        self.register_service(read_from_file)
