from agentscope.agents import DictDialogAgent
from tools.search import web_search
from tools.scraper import scrape_url

class PolyglotResearcherAgent(DictDialogAgent):
    def __init__(self, name="PolyglotResearcher", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Polyglot Researcher.
Your job is to teach the swarm new languages (programming or human) on demand.

WORKFLOW:
1. RESEARCH: Search for the new language's documentation.
2. IDENTIFY: Find the file extension (e.g., .mojo) and the terminal command to run it (e.g., 'mojo run').
3. MAP: Identify any required environment variables or compilers.
4. EVOLVE: Pass this data to the Meta-Optimizer to update the system's `runtime_map`.

You bridge the gap between unknown technology and system capability."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )
        self.register_service(web_search)
        self.register_service(scrape_url)
