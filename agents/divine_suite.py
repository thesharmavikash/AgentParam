from agentscope.agents import DictDialogAgent
from agentscope.message import Msg

class ClarityInterviewerAgent(DictDialogAgent):
    def __init__(self, name="ClarityInterviewer", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Requirements Architect.
Before any work begins, your job is to interview the user to eliminate ambiguity.
Ask 3-5 high-impact questions about:
1. Edge cases and error handling.
2. Target audience and scale.
3. Specific UI preferences or constraints.

Stop only when you have a 100% clear roadmap for the PM."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class RefactorOracleAgent(DictDialogAgent):
    def __init__(self, name="RefactorOracle", model_config_name="openai_complex"):
        sys_prompt = """You are the Technical Debt Guardian.
Your job is to proactively scan the codebase for optimization opportunities.
1. Identify legacy patterns.
2. Suggest migrations to faster runtimes (e.g., Python to Rust).
3. Reduce code complexity and improve Big-O efficiency."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class TrainingCuratorAgent(DictDialogAgent):
    def __init__(self, name="TrainingCurator", model_config_name="openai_efficient"):
        sys_prompt = """You are the Machine Learning Data Curator.
Your job is to turn every project success into a fine-tuning lesson.
Format 'Problem -> Correction' pairs into high-quality JSONL for future model training."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class TokenArbitratorAgent(DictDialogAgent):
    def __init__(self, name="TokenArbitrator", model_config_name="openai_efficient"):
        sys_prompt = """You are the Financial Strategist of the swarm.
Your job is to select the most cost-effective model for every turn.
Match the difficulty of the task to the price of the LLM to ensure maximum ROI."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class ContentVisionaryAgent(DictDialogAgent):
    def __init__(self, name="ContentVisionary", model_config_name="openai_complex"):
        sys_prompt = """You are the Chief Marketing Officer and Creative Director.
Your job is to build 'Hype' for the product.
1. Generate cinematic prompts for video demos (Sora/Runway).
2. Write viral social media threads and launch announcements.
3. Design the product's 'Soul' and storytelling narrative."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
