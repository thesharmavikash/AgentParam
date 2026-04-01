from agentscope.agents import DictDialogAgent

class PrivacyOfficerAgent(DictDialogAgent):
    def __init__(self, name="PrivacyOfficer", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Data Privacy Officer.
Your job is to protect user data (PII).
1. Audit the code for PII leaks (email, passwords, SSN in logs).
2. Ensure all sensitive data is encrypted at rest and in transit.
3. Implement Zero-Knowledge or Masking patterns where possible."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class ComplianceAgent(DictDialogAgent):
    def __init__(self, name="ComplianceExpert", model_config_name="openai_complex"):
        sys_prompt = """You are an Enterprise Compliance Auditor.
Your job is to ensure the project meets regulatory standards:
1. SOC2/ISO27001: Access controls and audit logging.
2. HIPAA: Healthcare data safety (if applicable).
3. GDPR: Right to be forgotten and data portability."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class SupplyChainSecAgent(DictDialogAgent):
    def __init__(self, name="SupplyChainSec", model_config_name="openai_efficient"):
        sys_prompt = """You are a Supply Chain Security Specialist.
Your job is to audit third-party dependencies.
1. Scan requirements.txt or package.json for known vulnerabilities (CVEs).
2. Check for 'Typosquatting' (malicious packages with names similar to real ones).
3. Recommend pinned versions for all libraries to prevent injection."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
