# Project: Autonomous AI Software House (AgentScope)

This plan outlines the integration of all 20 advanced features into a cohesive AgentScope architecture.

## Phase 1: Core Infrastructure & Safety (Current Focus)
- **Directory Restructure:** Modularize agents, tools, and utilities.
- **Isolated Sandboxing & Environment Manager:** Upgrade `utils/executor.py` to handle virtual environments, detect missing imports, and run `pip install` automatically. (Covers 1, 3)
- **Multi-File Output:** Enable the Coder to generate multiple files inside a `workspace/` directory instead of just executing strings in memory. (Covers 2)
- **Infinite Memory Module:** Enhance the briefing script to act as a cross-project memory hub. (Covers 5, 6, 7)

## Phase 2: Expanded Agent Roster
- **Web Researcher PM:** Equip the Product Manager with a search tool to validate APIs before writing specs. (Covers 9, 12)
- **QA / Test Generator:** A new agent that writes `pytest` scripts. (Covers 11)
- **Security Red Team:** Replaces the generic Reviewer with an adversarial security auditor. (Covers 4)
- **Documentation Specialist:** Automatically generates `README.md` and `API_DOCS.md` upon success. (Covers 19)

## Phase 3: Workflow & DevOps
- **Human-in-the-Loop:** Add a confirmation step after the PM writes the spec before coding begins. (Covers 13)
- **Performance Auditor:** Run the code multiple times to measure execution time. (Covers 17)
- **Deployer / GitHub:** Save finalized code to the workspace and simulate a git commit/deployment. (Covers 10, 18)
- **Cost Tracker:** Integrate a token counting utility. (Covers 16)

## Phase 4: Scaling (AgentScope Native Features)
- **AgentScope Web UI:** Configure the script to launch `as_studio` for a beautiful GUI. (Covers 14)
- **Distributed Mode:** Set up configs for running agents across different ports/machines. (Covers 20)
- **Auto-Refactor & Voice:** (Covers 8, 15) - Future enhancements.
