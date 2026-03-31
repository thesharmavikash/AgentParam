from agentscope.agents import DictDialogAgent
from agentscope.message import Msg
import os
import shutil
import json

class LibrarianAgent(DictDialogAgent):
    def __init__(self, name="Librarian", model_config_name="openai_efficient"):
        sys_prompt = """You are the Enterprise Librarian.
Your job is to manage the 'Shared Library' of the AI Holding Company.
1. ARCHIVING: When a project is complete, you save its final code/reports into `shared_library/`.
2. RETRIEVAL: When a new project starts, you check if a similar solution already exists to save time and tokens.
3. INDEXING: You maintain a `library_index.json` with descriptions of all stored assets.

When asked to search, look at the index and recommend the best existing assets."""
        
        super().__init__(
            name=name,
            sys_prompt=sys_prompt,
            model_config_name=model_config_name
        )

    def archive_project(self, project_name, source_path):
        """Copies project files to the shared library and updates the index."""
        dest_path = os.path.join("shared_library", project_name)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(source_path, dest_path)
        
        # Update Index
        index_file = "shared_library/library_index.json"
        index = {}
        if os.path.exists(index_file):
            with open(index_file, "r") as f:
                index = json.load(f)
        
        index[project_name] = {
            "path": dest_path,
            "timestamp": str(os.path.getmtime(dest_path))
        }
        
        with open(index_file, "w") as f:
            json.dump(index, f, indent=4)
        
        return f"Project '{project_name}' archived to Shared Library."

    def reply(self, x: Msg = None) -> Msg:
        # Check if this is an archival request
        if "ARCHIVE_PROJECT:" in x.content:
            try:
                p_name = x.content.split("ARCHIVE_PROJECT:")[1].strip()
                # Find project workspace
                for root, dirs, files in os.walk("companies"):
                    if p_name in dirs and "projects" in root:
                        full_path = os.path.join(root, p_name)
                        msg = self.archive_project(p_name, full_path)
                        return Msg(self.name, msg, role="assistant")
                return Msg(self.name, f"Could not find workspace for {p_name}", role="assistant")
            except Exception as e:
                return Msg(self.name, f"Archival failed: {e}", role="assistant")
        
        return super().reply(x)
