import os
import ast
from agentscope.service import ServiceResponse

def view_file_summary(file_path: str) -> ServiceResponse:
    """
    ACI Tool: Returns a summary of a Python file (classes, functions, docstrings)
    without returning the entire file contents. Essential for saving context window.
    """
    if not os.path.exists(file_path):
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"File not found: {file_path}")
    
    if not file_path.endswith('.py'):
        # For non-python files, just return the first 20 lines as a preview
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:20]
            return ServiceResponse(status=ServiceResponse.SUCCESS, content="Preview:\n" + "".join(lines) + "\n...(truncated)")
        except Exception as e:
            return ServiceResponse(status=ServiceResponse.ERROR, content=str(e))

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        tree = ast.parse(code)
        summary = []
        
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                summary.append(f"class {node.name}:")
                for sub_node in node.body:
                    if isinstance(sub_node, ast.FunctionDef):
                        summary.append(f"    def {sub_node.name}():")
            elif isinstance(node, ast.FunctionDef):
                summary.append(f"def {node.name}():")
                
        return ServiceResponse(status=ServiceResponse.SUCCESS, content="\n".join(summary) if summary else "No classes or functions found.")
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Parse error: {str(e)}")

def search_repository(directory: str, pattern: str) -> ServiceResponse:
    """
    ACI Tool: Searches for a string pattern across all files in a directory.
    """
    import glob
    results = []
    try:
        files = glob.glob(f"{directory}/**/*", recursive=True)
        for filepath in files:
            if os.path.isfile(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for i, line in enumerate(f):
                            if pattern in line:
                                results.append(f"{filepath}:{i+1}: {line.strip()}")
                except UnicodeDecodeError:
                    pass # Skip binary files
        
        if not results:
            return ServiceResponse(status=ServiceResponse.SUCCESS, content="No matches found.")
        
        # Limit to top 50 results to protect context
        return ServiceResponse(status=ServiceResponse.SUCCESS, content="\n".join(results[:50]))
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=str(e))
