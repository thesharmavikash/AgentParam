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
    print("🚀 AgentScope v31.0 - THE SOVEREIGN ENTITY (Biological & Legal Integration) 🚀")
    
    # 1. Company Selection
    available_companies = [d for d in os.listdir("companies") if os.path.isdir(os.path.join("companies", d))]
    selected_company = input(f"Login to Swarm Node {available_companies}: ") or available_companies[0]
    
    project_name = "sovereign_entity_mission"
    briefing = init_project(project_name)

    # 2. Initialize Sovereignty Board
    manager = get_agent_instance("LeadOrchestrator", project_name, "openai_complex", briefing)
    entity_architect = get_agent_instance("LegalEntitySRE", project_name, "openai_complex", briefing)
    user = UserAgent(name="User")
    
    # --- 1. BIO-RESONANCE (Neural Focus Bridge) ---
    print("\n🔗 [Bio-Bridge] Syncing with user focus metrics...")
    # Simulation: In real use, this would read from an API/Wearable
    focus = 85 # Simulated: User is in Deep Work
    stress = 10 # Simulated: User is calm
    bio_mode = cost_tracker.update_bio_metrics(focus, stress)
    print(f"🧠 [Bio-Bridge] Resonance: {bio_mode} (Focus: {focus}%, Stress: {stress}%)")

    objective_text = user.query("\nEnter Supreme Objective: ")
    current_context = Msg("User", f"OBJECTIVE: {objective_text}\nBIO_MODE: {bio_mode}", role="user")

    # --- START SOVEREIGN SWARM ---
    with msghub([manager, user]) as hub:
        for turn in range(50):
            decision = manager(current_context)
            cost_tracker.update(decision)
            
            if "PROJECT_COMPLETE" in decision.content:
                print("\n🏆 SOVEREIGN ENTITY ESTABLISHED 🏆")
                break

            # 2. LEGAL ACTION: FORM ENTITY
            if "FORM_LEGAL_ENTITY:" in decision.content:
                print("\n⚖️ [LegalSRE] Drafting Articles of Incorporation...")
                entity_res = entity_architect(decision)
                current_context = entity_res
                continue

            # 3. Standard Routing
            try:
                agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
                task = decision.content.split("TASK:")[1].strip()
                
                agent = get_agent_instance(agent_name, project_name, "openai_complex", briefing)
                if agent:
                    # Adjust turn duration based on focus mode
                    if "SILENT_EXECUTION" in bio_mode:
                        print(f"--- [Quiet Mode] {agent_name} is processing in background... ---")
                    else:
                        print(f"--- Routing to {agent_name} ---")
                        
                    agent_msg = agent(Msg("Manager", task, role="user"))
                    cost_tracker.update(agent_msg)
                    current_context = agent_msg
            except:
                current_context = Msg("System", "Neural heartbeat...", role="user")

    print(f"\n🏁 Session Complete. Sovereign Genome generated. Entity finalized.")

if __name__ == "__main__":
    main()
Applied fuzzy match at line 1-100.