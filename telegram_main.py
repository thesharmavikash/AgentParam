import os
import json
import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import agentscope
from agentscope.message import Msg
from agentscope.msghub import msghub

from agents.pm import ProductManagerAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.reviewer import RedTeamReviewerAgent
from agents.docs import DocsAgent
from agents.qa import QAAgent
from agents.devops import DevOpsAgent
from agents.manager import ManagerAgent
from utils.tracker import cost_tracker
from memory.history import get_project_briefing

# Load Config
with open("configs/telegram_config.json", "r") as f:
    tg_config = json.load(f)

BOT_TOKEN = tg_config["bot_token"]

async def run_swarm_logic(update: Update, context: ContextTypes.DEFAULT_TYPE, objective: str):
    chat_id = update.effective_chat.id
    project_name = f"tg_proj_{update.effective_user.id}"
    
    await context.bot.send_message(chat_id=chat_id, text=f"🚀 Swarm Initialized for Project: {project_name}\nTarget: {objective[:100]}...")

    # Initialize AgentScope (Silent mode for background run)
    agentscope.init(
        model_configs="./configs/model_configs.json",
        project=project_name,
        save_log=True
    )
    
    briefing = get_project_briefing(project_name)

    # Setup Team
    manager = ManagerAgent()
    pm = ProductManagerAgent(briefing=briefing)
    coder = CoderAgent(project_name=project_name)
    tester = TesterAgent(project_name=project_name)
    reviewer = RedTeamReviewerAgent()
    docs = DocsAgent(project_name=project_name)
    qa = QAAgent(project_name=project_name)
    devops = DevOpsAgent(project_name=project_name)

    team = {
        "ProductManager": pm, "Coder": coder, "Tester": tester,
        "SecurityReviewer": reviewer, "DocumentationSpecialist": docs,
        "QAAgent": qa, "DevOps": devops
    }

    # Swarm Loop
    current_context = Msg("User", objective, role="user")
    
    # Custom loop to send updates to Telegram
    for turn in range(20):
        decision = manager(current_context)
        
        if "PROJECT_COMPLETE" in decision.content:
            await context.bot.send_message(chat_id=chat_id, text="🏆 PROJECT COMPLETE! 🏆\nFiles are ready in the workspace.")
            break
            
        try:
            agent_name = decision.content.split("NEXT_AGENT:")[1].split("\n")[0].strip()
            task = decision.content.split("TASK:")[1].strip()
            
            if agent_name in team:
                status_msg = await context.bot.send_message(chat_id=chat_id, text=f"⏳ {agent_name} is working...")
                
                # Execute agent
                agent_msg = team[agent_name](Msg("Manager", task, role="user"))
                
                # Update Telegram with a snippet of the result
                preview = agent_msg.content[:300] + "..." if len(agent_msg.content) > 300 else agent_msg.content
                await context.bot.send_message(chat_id=chat_id, text=f"✅ {agent_name} Finished:\n{preview}")
                
                current_context = agent_msg
        except Exception as e:
            print(f"Error: {e}")
            break

    await context.bot.send_message(chat_id=chat_id, text=f"🏁 Session Finished. Total Cost: ${cost_tracker.get_report()['total_cost_usd']}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI Software House Bot. Send me a project description and I will build it for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    objective = update.message.text
    # Run swarm in background so bot stays responsive
    asyncio.create_task(run_swarm_logic(update, context, objective))

import openai # For Whisper transcription

# ... (previous imports)

async def transcribe_voice(file_path: str) -> str:
    """Transcribes audio using OpenAI Whisper."""
    try:
        client = openai.OpenAI(api_key=tg_config.get("openai_api_key") or "YOUR_OPENAI_KEY")
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        return f"Transcription error: {str(e)}"

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="🎙️ Receiving voice note... Transcribing...")
    
    # 1. Download voice file
    voice_file = await context.bot.get_file(update.message.voice.file_id)
    os.makedirs("temp_audio", exist_ok=True)
    file_path = f"temp_audio/voice_{update.effective_user.id}.ogg"
    await voice_file.download_to_drive(file_path)
    
    # 2. Transcribe
    objective = await transcribe_voice(file_path)
    await context.bot.send_message(chat_id=chat_id, text=f"📝 Transcribed Objective:\n\"{objective}\"\n\n🚀 Starting Swarm...")
    
    # 3. Clean up
    if os.path.exists(file_path):
        os.remove(file_path)
        
    # 4. Trigger Swarm
    asyncio.create_task(run_swarm_logic(update, context, objective))

if __name__ == "__main__":
    print("🤖 Telegram Bot Bridge Starting...")
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice)) # 🎤 New Voice Handler
    
    application.run_polling()
