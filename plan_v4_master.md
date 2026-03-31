# Master-Tier Enterprise Upgrade Plan (v10.0)

## 1. Codebase Oracle (Vector RAG Memory)
- **Component:** `memory/vector_db.py`
- **Action:** Integrate `chromadb` to index all code files in the `workspace/`.
- **Integration:** Give the `CoderAgent` a `query_codebase` tool so it can semantically search for functions and context across thousands of files.

## 2. Autonomous Documentation Browser (Live Learning)
- **Component:** `tools/scraper.py`
- **Action:** Build a real web scraper using `BeautifulSoup` to fetch live documentation.
- **Integration:** Update `ProductManagerAgent` to use `scrape_url` to learn new APIs on the fly before writing specs.

## 3. "The Eyes" (Vision-Based QA)
- **Component:** `tools/browser_tool.py` & `agents/qa.py`
- **Action:** Upgrade the Playwright browser tool to capture base64 screenshots.
- **Integration:** The `QAAgent` will receive the screenshot and use Vision models (GPT-4o) to verify UI/UX correctness (e.g., overlapping buttons, bad contrast).

## 4. The "Fortress" Sandbox (Docker Execution)
- **Component:** `utils/executor.py`
- **Action:** Integrate the Python `docker` SDK.
- **Integration:** When executing code, attempt to spin up an ephemeral Docker container (e.g., `python:3.11-slim`). If Docker is unavailable, fallback to the strict sub-process sandbox.

## 5. Multi-Agent "War Room" (Debate Mechanism)
- **Component:** `agents/manager.py`
- **Action:** Enhance the Lead Orchestrator to trigger a "Debate" state.
- **Integration:** If a complex technical decision is needed, the Manager spawns two Reviewers to argue different architectures, and the Planner makes the final call.
