# Multi-Agent Evolution Plan (v12.0)

## 1. The Agent Marketplace (Dynamic Hiring)
- **Concept:** The Manager can now "instantiate" specialized sub-agents on the fly.
- **New Agents:** `UIDesigner`, `DBArchitect`, `DevOpsSRE`.
- **Logic:** Instead of a static team, the `ManagerAgent` will have a tool to `spawn_specialist(role_name)` when the project requires specific expertise.

## 2. Peer-Review Consensus (The "Double Coder" Debate)
- **Concept:** For critical logic, the system triggers a "Parallel Implementation" phase.
- **Mechanism:** Two `CoderAgents` (e.g., one on GPT-4o and one on Claude 3.5) propose code. A `JudgeAgent` runs both, compares performance/security, and merges the best parts.

## 3. Collective Knowledge Graph (Shared Experience)
- **Concept:** A global memory that persists across ALL projects.
- **Action:** Agents write to `global_lessons_learned` in ChromaDB.
- **Benefit:** If a `Tester` finds a bug in a Flask project, the `Coder` in a future Django project will be warned about similar logic pitfalls.

## 4. Adversarial Client Simulator (Persona Mode)
- **Component:** `agents/client_sim.py`.
- **Action:** An agent that simulates "Scope Creep" or "Vague Requirements" to test the `ProductManager`'s ability to create rigid specs.

## 5. Formalized Distributed Swarm
- **Action:** Update `main.py` to allow assigning specific agents to specific IP addresses/ports, enabling a true multi-server development swarm.
