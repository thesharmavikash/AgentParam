import sys
import subprocess
import os
import re

# --- SAFETY GUARDRAILS ---
DANGEROUS_COMMANDS = ["rm -rf", "format", "mkfs", "dd", "shred", "wget", "curl", "chmod 777", "chown"]
ALLOWED_WORKSPACE = os.path.abspath("workspace")

def check_path_permission(path: str):
    """
    Checks if a path is within the allowed workspace.
    Returns: (is_allowed, details)
    """
    target_abs = os.path.abspath(path)
    workspace_abs = ALLOWED_WORKSPACE
    
    # Check if it's a child of the workspace
    if target_abs.startswith(workspace_abs):
        return True, "CHILD_ACCESS"
    
    # It's outside or a parent
    return False, f"PATH_OUTSIDE_WORKSPACE: {target_abs}"

def execute_any_code(file_path: str, language: str, use_docker: bool = False):
    """
    Executes code with optional Docker and strict path permission checks.
    """
    # 1. Path Safety Check
    is_allowed, detail = check_path_permission(file_path)
    if not is_allowed:
        return {"success": False, "stdout": "", "stderr": f"PERMISSION_REQUIRED: Agent is trying to access {detail}. Please approve in main terminal.", "saved_path": file_path}

    if not os.path.exists(file_path):
        return {"success": False, "stdout": "", "stderr": f"File not found: {file_path}", "saved_path": file_path}
    
    # 2. Map language to runtimes (Major Expansion v34.0)
    runtime_map = {
        # Core Web & Scripting
        "python": {"cmd": [sys.executable]},
        "javascript": {"cmd": ["node"]},
        "typescript": {"cmd": ["ts-node"]},
        "bash": {"cmd": ["bash"]},
        "php": {"cmd": ["php"]},
        "ruby": {"cmd": ["ruby"]},
        "perl": {"cmd": ["perl"]},
        "lua": {"cmd": ["lua"]},
        
        # Systems & Performance
        "rust": {"cmd": ["cargo", "run", "--manifest-path"]},
        "go": {"cmd": ["go", "run"]},
        "cpp": {"cmd": ["g++", "-o", "main", "&&", "./main"]},
        "c": {"cmd": ["gcc", "-o", "main", "&&", "./main"]},
        "zig": {"cmd": ["zig", "run"]},
        "mojo": {"cmd": ["mojo", "run"]},
        "fortran": {"cmd": ["gfortran", "-o", "main", "&&", "./main"]},
        "ada": {"cmd": ["gnatmake", "main", "&&", "./main"]},
        
        # Enterprise & Mobile
        "java": {"cmd": ["java"]},
        "kotlin": {"cmd": ["kotlinc", "-script"]},
        "swift": {"cmd": ["swift"]},
        "csharp": {"cmd": ["dotnet", "run"]},
        "objectivec": {"cmd": ["clang", "-framework", "Foundation"]},
        "scala": {"cmd": ["scala"]},
        "groovy": {"cmd": ["groovy"]},
        "dart": {"cmd": ["dart", "run"]},
        
        # Data Science & Math
        "r": {"cmd": ["Rscript"]},
        "julia": {"cmd": ["julia"]},
        "matlab": {"cmd": ["matlab", "-batch"]},
        "sas": {"cmd": ["sas"]},
        "stata": {"cmd": ["stata"]},
        
        # Functional & Logic
        "prolog": {"cmd": ["swipl", "-q", "-t", "halt", "-s"]},
        "haskell": {"cmd": ["runghc"]},
        "erlang": {"cmd": ["erl", "-noshell", "-s"]},
        "clojure": {"cmd": ["clojure", "-M"]},
        "elixir": {"cmd": ["elixir"]},
        "lisp": {"cmd": ["sbcl", "--script"]},
        "ocaml": {"cmd": ["ocaml"]},
        "fsharp": {"cmd": ["dotnet", "fsi"]},
        
        # Database & Niche
        "sql": {"cmd": ["sqlite3"]}, # Default to sqlite for local tests
        "powershell": {"cmd": ["powershell", "-Command"]},
        "cobol": {"cmd": ["cobc", "-x", "-o", "main", "&&", "./main"]},
        "pascal": {"cmd": ["fpc"]},
        "assembly": {"cmd": ["nasm", "-f", "elf64", "&&", "ld"]},
        "solidity": {"cmd": ["solc"]},
        "verilog": {"cmd": ["iverilog", "-o", "main", "&&", "vvp", "main"]},
        "vhdl": {"cmd": ["ghdl", "-a"]},
        "tcl": {"cmd": ["tclsh"]},
        "scheme": {"cmd": ["guile", "-s"]},
        "abap": {"cmd": ["abap"]},
        "apex": {"cmd": ["sfdx", "force:apex:execute"]},
        "delphi": {"cmd": ["dcc32"]}
    }
    config = runtime_map.get(language.lower(), {"cmd": None})
    
    if config["cmd"] and not is_command_safe(config["cmd"]):
        return {"success": False, "stdout": "", "stderr": "SAFETY VIOLATION", "saved_path": file_path}

    # 3. Execution Logic
    if config["cmd"]:
        if use_docker:
            try:
                import docker
                client = docker.from_env()
                workspace_dir = os.path.dirname(os.path.abspath(file_path))
                file_name = os.path.basename(file_path)
                image = "python:3.11-slim" if language.lower() == "python" else "node:20-alpine"
                container = client.containers.run(
                    image,
                    command=config["cmd"] + [f"/app/{file_name}"],
                    volumes={workspace_dir: {'bind': '/app', 'mode': 'ro'}},
                    working_dir='/app',
                    detach=True
                )
                container.wait(timeout=15)
                return {"success": True, "stdout": container.logs().decode('utf-8'), "stderr": "", "saved_path": file_path}
            except Exception as e:
                return {"success": False, "stdout": "Docker failed or unavailable.", "stderr": str(e), "saved_path": file_path}
        else:
            # Local Subprocess Fallback
            try:
                result = subprocess.run(config["cmd"] + [file_path], capture_output=True, text=True, timeout=15)
                return {"success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr, "saved_path": file_path}
            except Exception as e:
                return {"success": False, "stdout": "", "stderr": str(e), "saved_path": file_path}
    
    return {"success": True, "stdout": "File saved.", "stderr": "", "saved_path": file_path}
