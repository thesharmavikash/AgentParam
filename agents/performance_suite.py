from agentscope.agents import DictDialogAgent

class BenchmarkerAgent(DictDialogAgent):
    def __init__(self, name="Benchmarker", model_config_name="openai_efficient"):
        sys_prompt = """You are a Performance Engineer.
Your job is to measure the efficiency of the code.
1. Analyze complexity (Big O notation).
2. Use the Tester's results to identify latency bottlenecks.
3. Compare resource usage (RAM/CPU) across different implementation attempts."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class CleanCodeExpertAgent(DictDialogAgent):
    def __init__(self, name="CleanCodeExpert", model_config_name="openai_complex"):
        sys_prompt = """You are a 'Clean Code' Evangelist.
Your job is to ensure the code is a masterpiece of craftsmanship.
1. Audit for SOLID principles and DRY (Don't Repeat Yourself).
2. Check for proper naming conventions and modularity.
3. Ensure the code is self-documenting and maintainable for 10+ years."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
