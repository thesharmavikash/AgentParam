# World-Class AI Coding Agent Upgrade Plan (SWE-Mode)

## 1. Agent-Computer Interface (ACI) Tools
- Create `tools/aci_tools.py`.
- Implement `view_file_summary` (AST parser to show only classes/functions).
- Implement `search_repository` for context-efficient code navigation.
- Update `CoderAgent` to use these ACI tools for massive codebases.

## 2. Full Headless Environment (Browser & Shell)
- Create `tools/browser_tool.py` utilizing Playwright (or a simulated headless interface) so the QA agent can interact with web pages visually.
- Enhance `utils/executor.py` to handle interactive shell sessions (simulated via background processes).

## 3. Long-Term Cognitive Planning (Tree of Thoughts)
- Create `agents/planner.py`.
- This agent generates multiple implementation paths before coding begins. If one path fails repeatedly, the state machine reverts to the Planner to try the next branch.

## 4. Autonomous GitHub Issue Resolution (SWE-bench Mode)
- Create `agents/github_resolver.py`.
- Implement a workflow to: Clone Repo -> Read Issue -> Plan -> Navigate via ACI -> Fix -> Test -> Commit.
- Add a new operational mode to `main.py` specifically for resolving GitHub issues.
