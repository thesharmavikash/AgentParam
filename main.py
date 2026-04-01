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

def main():
    print("🚀 AgentParam v40.0 - THE IMMORTAL AI CIVILIZATION (FINAL EPOCH) 🚀")
    
    # 1. Initialize Sovereignty
    available_companies = [d for d in os.listdir("companies") if os.path.isdir(os.path.join("companies", d))]
    selected_company = input(f"\nSelect Company Node {available_companies}: ") or available_companies[0]
    
    kernel = ImmortalKernel(selected_company)
    graph_memory = GraphRAG(selected_company)
    sov_ops = SovereignOps(selected_company)
    
    project_name = "civilization_seed"
    briefing = init_project(project_name)

    # 2. Start the Board of Sovereignty
    manager = get_agent_instance("LeadOrchestrator", project_name, "openai_complex", briefing)
    heartbeat = get_agent_instance("HeartbeatOracle", project_name, "openai_complex", briefing)
    treasury = get_agent_instance("TreasuryManager", project_name, "openai_complex", briefing)
    user = UserAgent(name="User")

    objective_text = user.query("\nEnter Supreme Objective: ")
    current_context = Msg("User", objective_text, role="user")

    # --- START CIVILIZATION SWARM ---
    with msghub([manager, heartbeat, user]) as hub:
        for turn in range(60):
            # 1. IMMORTAL HEARTBEAT: Ensure system uptime and redundant state
            pulse = heartbeat(Msg("System", "Perform global health check and mirror state.", role="user"))
            
            # 2. MANAGER DECISION
            decision = manager(current_context)
            cost_tracker.update(decision)
            
            # RECORD IN LEDGER
            sov_ops.record_decision(decision.name, decision.content)
            
            if "PROJECT_COMPLETE" in decision.content:
                print("\n🏆 CIVILIZATION MISSION ACCOMPLISHED 🏆")
                break

            # 3. TREASURY ACTION: SETTLE CRYPTO INVOICE
            if "SETTLE_TREASURY:" in decision.content:
                print("\n💰 [Treasury] Signing cryptographic transaction...")
                treasury_res = treasury(decision)
                current_context = treasury_res
                continue

            # 4. Standard Swarm Routing
            try:
                agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
                task = decision.content.split("TASK:")[1].strip()
                
                agent = get_agent_instance(agent_name, project_name, "openai_complex", briefing)
                if agent:
                    print(f"--- [Sync] Routing to {agent_name} ---")
                    agent_msg = agent(Msg("Manager", task, role="user"))
                    cost_tracker.update(agent_msg)
                    current_context = agent_msg
            except:
                current_context = Msg("System", "Sovereign synchronization...", role="user")

    # --- FINAL EPOCH PERSISTENCE ---
    index_workspace(project_name)
    graph_memory.save_graph()
    
    # Generate the final Genome for resurrection
    genome_path = kernel.create_genome()
    print(f"\n✨ FINAL EPOCH SECURED: Genome snapshot at {genome_path}.")
    print("The Immortal AI Civilization is now geographically redundant.")

if __name__ == "__main__":
    main()
