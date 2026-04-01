from agents.pm import ProductManagerAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.reviewer import RedTeamReviewerAgent
from agents.security_expert import SecurityExpertAgent
from agents.docs import DocsAgent
from agents.qa import QAAgent
from agents.media import MediaAgent
from agents.devops import DevOpsAgent
from agents.planner import PlannerAgent
from agents.judge import JudgeAgent
from agents.client_sim import ClientSimAgent
from agents.searcher import SearcherAgent
from agents.summarizer import SummarizerAgent
from agents.strategist import StrategistAgent
from agents.sentinel import SentinelAgent
from agents.legal import LegalAdvisorAgent
from agents.seo import SEOExpertAgent
from agents.psychologist import UXPsychologistAgent
from agents.reasoning import ReasoningAgent
from agents.polyglot import PolyglotResearcherAgent

def get_agent_instance(agent_role, project_name, model_config, briefing=""):
    """
    Factory function to instantiate any agent from the shared pool.
    """
    registry = {
        "Planner": lambda: PlannerAgent(model_config_name=model_config),
        "ProductManager": lambda: ProductManagerAgent(briefing=briefing, model_config_name=model_config),
        "Coder": lambda: CoderAgent(name="Coder", project_name=project_name, model_config_name=model_config),
        "ParallelCoder": lambda: CoderAgent(name="ParallelCoder", project_name=project_name, model_config_name=model_config),
        "Tester": lambda: TesterAgent(project_name=project_name),
        "SecurityReviewer": lambda: RedTeamReviewerAgent(model_config_name=model_config),
        "SecurityExpert": lambda: SecurityExpertAgent(model_config_name=model_config),
        "DocumentationSpecialist": lambda: DocsAgent(project_name=project_name, model_config_name=model_config),
        "QAAgent": lambda: QAAgent(project_name=project_name, model_config_name=model_config),
        "DevOps": lambda: DevOpsAgent(project_name=project_name),
        "Searcher": lambda: SearcherAgent(model_config_name=model_config),
        "Summarizer": lambda: SummarizerAgent(model_config_name=model_config),
        "Strategist": lambda: StrategistAgent(project_name=project_name, model_config_name=model_config),
        "SwarmJudge": lambda: JudgeAgent(model_config_name=model_config),
        "DifficultClient": lambda: ClientSimAgent(model_config_name=model_config),
        "Librarian": lambda: LibrarianAgent(model_config_name=model_config),
        "Sentinel": lambda: SentinelAgent(model_config_name=model_config),
        "LegalAdvisor": lambda: LegalAdvisorAgent(project_name=project_name, model_config_name=model_config),
        "SEOExpert": lambda: SEOExpertAgent(model_config_name=model_config),
        "UXPsychologist": lambda: UXPsychologistAgent(model_config_name=model_config),
        "ReasoningExpert": lambda: ReasoningAgent(model_config_name=model_config),
        "PolyglotResearcher": lambda: PolyglotResearcherAgent(model_config_name=model_config)
    }

    return registry.get(agent_role, lambda: None)()
