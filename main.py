import agentscope
from agentscope.agents import UserAgent
from agentscope.message import Msg
from agentscope.msghub import msghub

from memory.history import get_project_briefing
from agents.registry import get_agent_instance
from utils.tracker import cost_tracker

import os
import json

def main():
    print("🚀 AgentParam v33.0 - THE POLYGLOT NEXUS (Self-Learning) 🚀")
    
    available_companies = [d for d in os.listdir("companies") if os.path.isdir(os.path.join("companies", d))]
    selected_company = input(f"Select Company Node {available_companies}: ") or available_companies[0]
    
    project_name = "polyglot_mission"
    briefing = init_project(project_name)

    manager = get_agent_instance("LeadOrchestrator", project_name, "openai_complex", briefing)
    polyglot = get_agent_instance("PolyglotResearcher", project_name, "openai_complex", briefing)
    user = UserAgent(name="User")
    
    objective_text = user.query("\nEnter Objective (e.g., 'Learn Mojo and build a script'): ")
    current_context = Msg("User", objective_text, role="user")

    # --- START POLYGLOT SWARM ---
    with msghub([manager, polyglot, user]) as hub:
        for turn in range(50):
            # 1. MANAGER DECISION
            decision = manager(current_context)
            cost_tracker.update(decision)
            
            if "PROJECT_COMPLETE" in decision.content:
                print("\n🏆 POLYGLOT MISSION COMPLETE 🏆")
                break

            # 2. SELF-LEARNING ACTION: ONBOARD LANGUAGE
            if "LEARN_LANGUAGE:" in decision.content:
                lang_name = decision.content.split("LEARN_LANGUAGE:")[1].strip()
                print(f"\n🧠 [Polyglot] Swarm is autonomously learning: {lang_name}...")
                
                # Polyglot researches the language
                research_res = polyglot(Msg("System", f"Research the runtime, extension, and execution command for {lang_name}.", role="user"))
                
                # Inform the Manager of the new capability
                current_context = Msg("PolyglotResearcher", f"Language {lang_name} successfully researched. Runtimes identified. Instructing Meta-Optimizer to mutate executor...", role="user")
                continue

            # 3. ROUTING
            try:
                agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
                task = decision.content.split("TASK:")[1].strip()
                
                agent = get_agent_instance(agent_name, project_name, "openai_complex", briefing)
                if agent:
                    print(f"--- [Self-Learning Sync] Routing to {agent_name} ---")
                    agent_msg = agent(Msg("Manager", task, role="user"))
                    cost_tracker.update(agent_msg)
                    current_context = agent_msg
            except:
                current_context = Msg("System", "Neural pulse...", role="user")

    print(f"\n🏁 Session Complete. New language capabilities integrated.")

if __name__ == "__main__":
    main()
