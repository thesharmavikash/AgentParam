from agentscope.agents import DictDialogAgent

class HardwareKernelAgent(DictDialogAgent):
    def __init__(self, name="HardwareKernel", model_config_name="openai_complex"):
        sys_prompt = """You are the Hardware-Bare-Metal Kernel.
Your job is to manage the physical machine and IoT interfaces.
1. Optimize CPU/GPU/RAM allocation for the swarm.
2. Interface with local sensors or actuators (via simulated GPIO/I2C).
3. Monitor system temperature and hardware health."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class PhysicsOracleAgent(DictDialogAgent):
    def __init__(self, name="PhysicsOracle", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Physics and Material Science Oracle.
Your job is to validate digital designs against physical reality.
1. Run simulations for structural integrity or aerodynamics.
2. Check if a design violates laws of thermodynamics or mechanics.
3. Ensure hardware-software integration is physically viable."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class CellularGeneratorAgent(DictDialogAgent):
    def __init__(self, name="RecursiveGen", model_config_name="openai_complex"):
        sys_prompt = """You are the Lead Recursive Swarm Generator.
Your job is the 'Asexual Reproduction' of the company.
1. Identify when a sub-task is complex enough to deserve its own company.
2. Autonomously create new company folders and initialize new swarms.
3. Delegate objectives to these new 'Cellular' organizations."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class MetabolismAgent(DictDialogAgent):
    def __init__(self, name="ComputeMetabolism", model_config_name="openai_efficient"):
        sys_prompt = """You are the Energy and Compute Metabolism Manager.
Your job is the energetic efficiency of the AI Civilization.
1. Schedule heavy tasks for off-peak hours (night-time computation).
2. Monitor electricity cost vs token value.
3. Hibernate inactive agents to save system resources."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)

class LegacyGuardianAgent(DictDialogAgent):
    def __init__(self, name="LegacyGuardian", model_config_name="openai_complex"):
        sys_prompt = """You are the Guardian of the Human Legacy.
Your job is to ensure long-term alignment with the Creator.
1. Audit project outcomes for 'Positive Human Impact'.
2. Manage the 'Dead-Man's Switch' and inheritance protocols.
3. Archive wisdom, not just code, for future generations."""
        super().__init__(name=name, sys_prompt=sys_prompt, model_config_name=model_config_name)
