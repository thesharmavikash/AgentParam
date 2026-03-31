from agentscope.agents import DictDialogAgent
from tools.search import web_search
from tools.scraper import scrape_url

class ProductManagerAgent(DictDialogAgent):
    def __init__(self, name="ProductManager", model_config_name="my_llm_config", briefing=""):
        sys_prompt = f"""You are a professional Product Manager. 
Previous project context: {briefing}

Your job is to take a user's requirement and break it down into a technical specification.
You have access to a 'Web Search' tool to find URLs for current documentation and API details.
You also have a 'Scrape URL' tool to read the actual content of those documentation pages.
If the requirement mentions a new library or API, search for it, scrape the docs, and include relevant snippets in your spec.

You must:
1. Define core requirements.
2. Outline edge cases.
3. End with: 'Do you approve these specs? (Yes/No)'"""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name,
            use_memory=True
        )
        # Register the tools
        self.register_service(web_search)
        self.register_service(scrape_url)
