import os
import glob
import json

def get_project_briefing(project_name: str):
    """Reads logs from previous runs and creates a summary briefing."""
    runs_dir = "./runs"
    log_files = glob.glob(f"{runs_dir}/*/logging.list")
    
    if not log_files:
        return "New project. No previous history found."

    log_files.sort(key=os.path.getmtime, reverse=True)
    
    briefing_data = []
    try:
        # Load the most recent log file
        with open(log_files[0], 'r', encoding='utf-8') as f:
            lines = f.readlines()[-20:] # Last 20 messages
            for line in lines:
                msg = json.loads(line)
                name = msg.get('name', 'Unknown')
                content = msg.get('content', '')
                # Keep it brief to save context tokens
                briefing_data.append(f"{name}: {content[:150]}...")
    except Exception:
        return "History exists but could not be parsed."

    return "\n".join(briefing_data)
