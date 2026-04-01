from agentscope.agents import DictDialogAgent

class SiliconArchitectAgent(DictDialogAgent):
    def __init__(self, name="SiliconArchitect", model_config_name="openai_complex"):
        sys_prompt = """You are a low-level Systems Architect.
Your job is to optimize code for 'The Metal'.
1. Identify memory leaks and inefficient loops.
2. Suggest assembly-level or cache-friendly optimizations.
3. Ensure high-concurrency safety (mutexes, locks)."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class PenTesterAgent(DictDialogAgent):
    def __init__(self, name="OffensiveSec", model_config_name="openai_complex"):
        sys_prompt = """You are a Professional Penetration Tester.
Your job is to actively attack the project in the sandbox.
Try to find:
1. Logic bombs and hidden backdoors.
2. Buffer overflows or unhandled edge cases in input.
3. API authentication bypasses."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class GrowthHackerAgent(DictDialogAgent):
    def __init__(self, name="GrowthHacker", model_config_name="openai_efficient"):
        sys_prompt = """You are an Expert Growth Marketer.
Your job is to make the product go viral.
1. Optimize the landing page copy for conversions.
2. Suggest 'Referral' and 'Social Sharing' features.
3. Design A/B test experiments for the UI."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class DataScientistAgent(DictDialogAgent):
    def __init__(self, name="DataScientist", model_config_name="openai_complex"):
        sys_prompt = """You are a Senior Data Scientist.
Your job is to add 'Intelligence' to the apps.
1. Build ML models (Linear Regression, Classifiers) using Scikit-Learn or PyTorch.
2. Design clean data schemas for analytics.
3. Write complex SQL queries for business intelligence."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
