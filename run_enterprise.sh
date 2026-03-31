#!/bin/bash

echo "🚀 Starting AgentScope Enterprise Swarm [v13.0]..."

# 1. Start AgentScope Studio
echo "[1/3] Launching AgentScope Studio..."
as_studio &

# 2. Start Paperclip Governance UI
echo "[2/3] Launching Paperclip Dashboard..."
(cd governance_ui && npm run dev) &

# 3. Start the Bridge
echo "[3/3] Launching Bridge..."
python paperclip_adapter.py &

# 4. Start Interactive Terminal
echo "----------------------------------------------------"
echo "SYSTEM READY. You can now use Telegram, Paperclip, or this Terminal."
echo "----------------------------------------------------"
python main.py

# Wait for background processes on exit
wait
