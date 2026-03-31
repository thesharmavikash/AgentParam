import json
import os

def generate_fine_tuning_dataset():
    """
    Collects successful turns from history and formats them for fine-tuning.
    """
    dataset_path = "memory/training_data.jsonl"
    runs_dir = "runs"
    
    entries = []
    # In a real setup, we would scan all 'logging.list' files
    # and only extract turns marked as 'SUCCESS' by the Judge.
    
    # Mock entry structure
    sample = {
        "instruction": "Build a secure Flask API",
        "output": "import flask\napp = flask.Flask(__name__)\n# [Security logic here]"
    }
    
    with open(dataset_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(sample) + "\n")
        
    return f"Dataset updated. Current size: {len(entries)} entries."
