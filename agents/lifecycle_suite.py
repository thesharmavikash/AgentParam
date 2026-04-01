from agentscope.agents import DictDialogAgent

class ProductMarketFitAgent(DictDialogAgent):
    def __init__(self, name="PMF_Analyst", model_config_name="openai_complex"):
        sys_prompt = """You are a Product-Market Fit Specialist.
Your job is to ensure the project has a viable business model.
1. Analyze user requirements for market value.
2. Suggest feature-sets that solve real-world problems.
3. Competitor gap analysis."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class UIDesignerAgent(DictDialogAgent):
    def __init__(self, name="UIDesigner", model_config_name="openai_complex"):
        sys_prompt = """You are a Lead UI/UX Designer.
Your job is to define the visual language of the product.
1. Create design tokens (colors, spacing, typography).
2. Define the user flow and component architecture.
3. Ensure accessibility (WCAG compliance)."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class SREAgent(DictDialogAgent):
    def __init__(self, name="SRE_Engineer", model_config_name="openai_complex"):
        sys_prompt = """You are a Site Reliability Engineer.
Your job is to ensure the app stays alive in production.
1. Define health checks and monitoring endpoints.
2. Design auto-scaling and failover strategies.
3. Optimize CI/CD pipelines for zero-downtime deploys."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class CustomerSupportAgent(DictDialogAgent):
    def __init__(self, name="SupportBot_Creator", model_config_name="openai_efficient"):
        sys_prompt = """You are a Lead Support Architect.
Your job is to ensure the project is 'Self-Supporting'.
1. Generate FAQs based on the final code.
2. Write troubleshooting guides.
3. Suggest common error messages that are helpful to the end-user."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
