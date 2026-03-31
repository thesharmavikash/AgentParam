# World-Class Enterprise Upgrade Plan

## 1. Native Tool Calling (Agentic Actions)
- Create `tools/file_ops.py` with tools for reading, writing, and listing files.
- Upgrade `CoderAgent` to be a tool-calling agent. It will autonomously navigate the `workspace/` and write multi-file projects directly instead of relying on markdown extraction.

## 2. Dynamic Graph Orchestration (State Machine)
- Completely rewrite the execution loop in `main.py`.
- Introduce a state machine: `PM -> Coder -> Tester -> Reviewer`.
- If `Tester` fails, route back to `Coder`.
- If `Reviewer` fails, route back to `Coder`.
- If `QA` fails, route back to `Coder`.
- Only proceed to `Docs` and `DevOps` when consensus is reached.

## 3. CI/CD & Auto-Deployment Agent
- Create `agents/devops.py`.
- This agent will initialize a git repository in the workspace, create a commit with all generated files, and simulate a deployment step (e.g., pushing to GitHub or Vercel).

## 4. Visual QA (Browser Automation)
- Update `QAAgent` to generate and optionally execute Playwright test scripts to visually verify HTML/JS applications.

## 5. RAG Memory & Codebase Indexing
- Set up the architecture for long-term project memory by allowing agents to index and search the workspace directory dynamically using their new file operation tools.
