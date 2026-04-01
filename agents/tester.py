from agentscope.agents import AgentBase
from agentscope.message import Msg
from utils.executor import execute_python_code
import time

class TesterAgent(AgentBase):
    """An agent that extracts code from a message and executes it."""
    def __init__(self, name="Tester", project_name="default", **kwargs):
        super().__init__(name=name, **kwargs)
        self.project_name = project_name

    def reply(self, x: Msg = None) -> Msg:
        content = x.content
        language = "python" # Default
        
        # Comprehensive Extension-to-Language Mapping (v34.0)
        ext_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript', '.sh': 'bash',
            '.rs': 'rust', '.pl': 'prolog', '.go': 'go', '.java': 'java',
            '.cpp': 'cpp', '.cc': 'cpp', '.c': 'c', '.rb': 'ruby',
            '.php': 'php', '.kt': 'kotlin', '.swift': 'swift', '.cs': 'csharp',
            '.scala': 'scala', '.r': 'r', '.jl': 'julia', '.m': 'matlab',
            '.hs': 'haskell', '.erl': 'erlang', '.clj': 'clojure', '.ex': 'elixir',
            '.zig': 'zig', '.mojo': 'mojo', '.f90': 'fortran', '.sql': 'sql',
            '.ps1': 'powershell', '.cob': 'cobol', '.pas': 'pascal', '.sol': 'solidity'
        }
        
        import re
        file_path_match = re.search(r"workspace/[a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+", content)
        if file_path_match:
            file_path = file_path_match.group(0)
            # Find extension
            _, ext = os.path.splitext(file_path)
            language = ext_map.get(ext.lower(), "python")
        else:
            file_path = f"workspace/{self.project_name}/main.py"

        print(f"[{self.name}] Testing File: {file_path} (Language: {language})")
        from utils.executor import execute_any_code
        
        start_time = time.time()
        result = execute_any_code(file_path, language)
        execution_time = time.time() - start_time
        
        feedback = f"Execution Success: {result['success']}\n"
        feedback += f"Execution Time: {execution_time:.2f} seconds\n"
        
        if result['success']:
            feedback += f"Saved to: {result['saved_path']}\n"
            
        feedback += f"STDOUT:\n{result['stdout']}\n"
        
        if result['stderr']:
            feedback += f"STDERR:\n{result['stderr']}\n"
        
        if not result['success'] or result['stderr']:
            feedback += "\nACTION REQUIRED: Please fix the errors above and provide the updated code."
        else:
            feedback += "\nAll tests passed successfully! Ready for Security Review."

        res_msg = Msg(self.name, feedback, role="assistant")
        self.speak(res_msg)
        return res_msg
