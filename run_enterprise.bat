@echo off
echo 🚀 Starting AgentScope Enterprise Swarm [v13.0]...

:: 1. Start AgentScope Studio (Real-time Dashboard)
echo [1/3] Launching AgentScope Studio...
start "AgentScope Studio" cmd /c "as_studio"

:: 2. Start Paperclip Governance UI
echo [2/3] Launching Paperclip Dashboard...
:: Note: Assumes npm install has been run
start "Paperclip Dashboard" cmd /c "cd governance_ui && npm run dev"

:: 3. Start the Bridge and Interactive Terminal
echo [3/3] Launching Bridge & Controller...
echo ----------------------------------------------------
echo SYSTEM READY. You can now use Telegram, Paperclip, or this Terminal.
echo ----------------------------------------------------
python paperclip_adapter.py & python main.py

pause
