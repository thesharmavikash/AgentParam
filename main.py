import agentscope
from agentscope.agents import UserAgent
from agentscope.message import Msg
from agentscope.msghub import msghub

from memory.history import get_project_briefing
from memory.vector_db import query_global_knowledge, log_lesson_learned, index_workspace
from memory.graph_rag import GraphRAG

from agents.registry import get_agent_instance
from utils.tracker import cost_tracker
from utils.sovereign_ops import SovereignOps
from utils.immortal_kernel import ImmortalKernel

import os
import json

def init_project(project_name: str, use_gui: bool = False):
    agentscope.init(
        model_configs="./configs/model_configs.json",
        project=project_name,
        save_log=True,
        use_gui=use_gui
    )
    return get_project_briefing(project_name)

def main():
    print("🚀 AgentParam v38.0 - THE DIVINE ARCHITECTURE 🚀")
    
    # --- 1. MODE SELECTION ---
    available_companies = [d for d in os.listdir("companies") if os.path.isdir(os.path.join("companies", d))]
    selected_company = input(f"\nSelect Company Node {available_companies}: ") or available_companies[0]
    
    project_name = "divine_mission"
    briefing = init_project(project_name)

    # Initialize Core Sovereignty
    manager = get_agent_instance("LeadOrchestrator", project_name, "openai_complex", briefing)
    user = UserAgent(name="User")
    
    # --- 🎤 CLARITY INTERVIEW PHASE ---
    print("\n🎤 [ClarityInterviewer] Initiating architectural interview...")
    interviewer = get_agent_instance("ClarityInterviewer", project_name, "openai_complex", briefing)
    initial_objective = user.query("\nEnter your initial project objective: ")
    
    interview_q = interviewer(initial_objective)
    user_answers = user.query(f"\nPlease answer the following questions to finalize the spec:\n{interview_q.content}\n\nYour Answer: ")
    
    final_objective = Msg("User", f"OBJECTIVE: {initial_objective.content}\nINTERVIEW_ANSWERS: {user_answers.content}", role="user")
    current_context = final_objective

    # --- START DIVINE SWARM ---
    with msghub([manager, user]) as hub:
        for turn in range(60): # Increased turn limit for deeper logic
            decision = manager(current_context)
            cost_tracker.update(decision)
            
            if "PROJECT_COMPLETE" in decision.content:
                print("\n🏆 DIVINE MISSION COMPLETE 🏆")
                break

            try:
                agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
                task = decision.content.split("TASK:")[1].strip()
                
                agent = get_agent_instance(agent_name, project_name, "openai_complex", briefing)
                if agent:
                    print(f"--- [Divine Sync] Routing to {agent_name} ---")
                    agent_msg = agent(Msg("Manager", task, role="user"))
                    cost_tracker.update(agent_msg)
                    current_context = agent_msg
            except:
                current_context = Msg("System", "Neural heartbeat...", role="user")

    # --- 🏛️ REFACTOR ORACLE & CURATION PHASE ---
    print("\n🔮 [RefactorOracle] Scanning for technical debt and optimizations...")
    oracle = get_agent_instance("RefactorOracle", project_name, "openai_complex", briefing)
    oracle(current_context)

    print("\n📚 [TrainingCurator] Harvesting high-signal data for fine-tuning...")
    curator = get_agent_instance("TrainingCurator", project_name, "openai_efficient", briefing)
    curator(current_context)

    print(f"\n🏁 Session Complete. Sovereign Evolution Logged.")

if __name__ == "__main__":
    main()
