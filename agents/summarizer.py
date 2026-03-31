from agentscope.agents import DictDialogAgent

class SummarizerAgent(DictDialogAgent):
    def __init__(self, name="Summarizer", model_config_name="my_llm_config"):
        sys_prompt = """You are a Data Synthesis Expert.
Your job is to take the raw research provided by the Searcher and distill it into a concise executive summary.
Highlight:
- Key opportunities.
- Major threats.
- Pricing benchmarks.
Eliminate noise and focus on actionable data points."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
