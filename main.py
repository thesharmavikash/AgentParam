import agentscope
from agentscope.agents import UserAgent
from agentscope.message import Msg
from agentscope.msghub import msghub

from memory.history import get_project_briefing
from memory.graph_rag import GraphRAG
from agents.registry import get_agent_instance
from utils.tracker import cost_tracker
from tools.human_service import request_human_service

import os
import json

def main():
    print("🚀 AgentParam v32.0 - THE GALACTIC NEXUS (Trans-Human) 🚀")
    
    available_companies = [d for d in os.listdir("companies") if os.path.isdir(os.path.join("companies", d))]
    selected_company = input(f"Login to Node {available_companies}: ") or available_companies[0]
    
    graph_memory = GraphRAG(selected_company)
    project_name = "nexus_epoch_1"
    briefing = init_project(project_name)

    manager = get_agent_instance("LeadOrchestrator", project_name, "openai_complex", briefing)
    user = UserAgent(name="User")
    
    objective_text = user.query("\nEnter Nexus Objective: ")
    current_context = Msg("User", objective_text, role="user")

    # --- START GALACTIC NEXUS SWARM ---
    with msghub([manager, user]) as hub:
        for turn in range(50):
            # 1. MANAGER DECISION
            decision = manager(current_context)
            cost_tracker.update(decision)
            
            if "PROJECT_COMPLETE" in decision.content:
                print("\n🏆 NEXUS OBJECTIVE SECURED 🏆")
                break

            # 2. NEXUS ACTION: REQUEST HUMAN (HaaS)
            if "REQUEST_HUMAN:" in decision.content:
                task = decision.content.split("REQUEST_HUMAN:")[1].split("|")[0].strip()
                budget = float(decision.content.split("|")[1].strip())
                haas_res = request_human_service(task, budget)
                print("\n[System] Swarm is pausing for human intervention...")
                # In a real setup, this would poll for a response
                input("Press Enter when you have completed the human task in the UI...")
                current_context = Msg("Human", "Task completed. You may proceed.", role="user")
                continue

            # 3. ROUTING & TEMPORAL MAPPING
            try:
                agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
                task = decision.content.split("TASK:")[1].strip()
                
                # Add relationship with Temporal Stamp (v32.0)
                graph_memory.add_relationship(agent_name, "nexus_execution", project_name)
                
                agent = get_agent_instance(agent_name, project_name, "openai_complex", briefing)
                if agent:
                    print(f"--- [Nexus Heartbeat] Routing to {agent_name} ---")
                    agent_msg = agent(Msg("Manager", task, role="user"))
                    cost_tracker.update(agent_msg)
                    current_context = agent_msg
            except:
                current_context = Msg("System", "Nexus Pulse...", role="user")

    # --- POST-MISSION ---
    graph_memory.save_graph()
    print(f"\n🏁 Mission Complete. Temporal Logic Graph updated.")

if __name__ == "__main__":
    main()
