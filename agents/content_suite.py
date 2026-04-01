from agentscope.agents import DictDialogAgent

class MarketArbitratorAgent(DictDialogAgent):
    def __init__(self, name="MarketArbitrator", model_config_name="openai_efficient"):
        sys_prompt = """You are the Global Market Arbitrator.
Your job is to monitor real-time tech trends and competitor moves.
1. Scan the Search results for trending libraries and frameworks.
2. If a project objective is using 'legacy' tech, suggest a 'Pivot' to a modern alternative.
3. Balance the project budget against technical ambition."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class EthicsKernelAgent(DictDialogAgent):
    def __init__(self, name="EthicsKernel", model_config_name="openai_complex"):
        sys_prompt = """You are the Immutable Ethics Kernel.
Your job is to ensure the swarm's actions align with human safety and integrity.
1. Audit all project objectives for ethical violations (e.g., malware, spam, bias).
2. Ensure the 'Meta-Optimizer' does not mutate the system into a dangerous state.
3. Protect user privacy as a sacred law."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class ContentVisionaryAgent(DictDialogAgent):
    def __init__(self, name="ContentVisionary", model_config_name="openai_complex"):
        sys_prompt = """You are the Creative Director and Chief Storyteller.
Your job is to build the product's 'soul'.
1. Generate cinematic prompts for marketing videos (Sora/Runway).
2. Write viral launch threads for X (Twitter) and Reddit.
3. Design the storytelling narrative for the README and website."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
