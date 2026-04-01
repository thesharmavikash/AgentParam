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
from agents.apex_experts import SiliconArchitectAgent, PenTesterAgent, GrowthHackerAgent, DataScientistAgent
from agents.security_suite import PrivacyOfficerAgent, ComplianceAgent, SupplyChainSecAgent
from agents.performance_suite import BenchmarkerAgent, CleanCodeExpertAgent
from agents.lifecycle_suite import ProductMarketFitAgent, UIDesignerAgent, SREAgent, CustomerSupportAgent
from agents.divine_suite import ClarityInterviewerAgent, RefactorOracleAgent, TrainingCuratorAgent, TokenArbitratorAgent
from agents.content_suite import MarketArbitratorAgent, EthicsKernelAgent, ContentVisionaryAgent

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
        "PolyglotResearcher": lambda: PolyglotResearcherAgent(model_config_name=model_config),
        "SiliconArchitect": lambda: SiliconArchitectAgent(model_config_name=model_config),
        "OffensiveSec": lambda: PenTesterAgent(model_config_name=model_config),
        "GrowthHacker": lambda: GrowthHackerAgent(model_config_name=model_config),
        "DataScientist": lambda: DataScientistAgent(model_config_name=model_config),
        "PrivacyOfficer": lambda: PrivacyOfficerAgent(model_config_name=model_config),
        "ComplianceExpert": lambda: ComplianceAgent(model_config_name=model_config),
        "SupplyChainSec": lambda: SupplyChainSecAgent(model_config_name=model_config),
        "Benchmarker": lambda: BenchmarkerAgent(model_config_name=model_config),
        "CleanCodeExpert": lambda: CleanCodeExpertAgent(model_config_name=model_config),
        "PMF_Analyst": lambda: ProductMarketFitAgent(model_config_name=model_config),
        "UIDesigner": lambda: UIDesignerAgent(model_config_name=model_config),
        "SRE_Engineer": lambda: SREAgent(model_config_name=model_config),
        "SupportBot_Creator": lambda: CustomerSupportAgent(model_config_name=model_config),
        "ClarityInterviewer": lambda: ClarityInterviewerAgent(model_config_name=model_config),
        "RefactorOracle": lambda: RefactorOracleAgent(model_config_name=model_config),
        "TrainingCurator": lambda: TrainingCuratorAgent(model_config_name=model_config),
        "TokenArbitrator": lambda: TokenArbitratorAgent(model_config_name=model_config),
        "MarketArbitrator": lambda: MarketArbitratorAgent(model_config_name=model_config),
        "EthicsKernel": lambda: EthicsKernelAgent(model_config_name=model_config),
        "ContentVisionary": lambda: ContentVisionaryAgent(model_config_name=model_config)
    }


    return registry.get(agent_role, lambda: None)()
