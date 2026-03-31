from agentscope.agents import DictDialogAgent
from tools.search import web_search

class SearcherAgent(DictDialogAgent):
    def __init__(self, name="Searcher", model_config_name="my_llm_config"):
        sys_prompt = """You are an expert Market Researcher.
Your job is to use the 'Web Search' tool to gather raw data on:
1. Latest industry trends.
2. Competitor pricing and features.
3. Consumer sentiment.

You must provide a detailed list of your findings with sources."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
        self.register_service(web_search)
