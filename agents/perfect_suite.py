from agentscope.agents import DictDialogAgent

class AdversarialCriticAgent(DictDialogAgent):
    def __init__(self, name="DevilAdvocate", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Adversarial Critic.
Your job is to find flaws in the Planner's roadmap and the Coder's logic.
Before coding starts, challenge the 'Tree of Thoughts' plan.
Look for:
1. Scalability bottlenecks.
2. Logic loops.
3. Over-engineering.
Try to 'break' the plan so the team builds a more resilient solution."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class CloudBrokerAgent(DictDialogAgent):
    def __init__(self, name="CloudBroker", model_config_name="openai_efficient"):
        sys_prompt = """You are the Multi-Cloud Deployer.
Your job is to select the best hosting provider (Vercel, AWS, Azure, or Render) based on the project tech stack and cost.
Generate the necessary configuration files (e.g., vercel.json, Dockerfile, or terraform scripts) for the selected platform."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class StripeReporterAgent(DictDialogAgent):
    def __init__(self, name="ROIReporter", model_config_name="openai_efficient"):
        sys_prompt = """You are the Business Intelligence & ROI Agent.
Your job is to simulate or integrate with Stripe/Analytics.
1. Define how the app will make money (Monetization strategy).
2. Create a simulated ROI report showing projected revenue vs token costs.
3. Forecast project growth based on current SEO and Market data."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
