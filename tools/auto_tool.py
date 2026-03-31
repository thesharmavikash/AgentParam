import os
import importlib
import sys
from agentscope.service import ServiceResponse

def create_autonomous_tool(tool_name: str, code: str) -> ServiceResponse:
    """
    Allows an agent to write its own Python tool and register it to the system.
    """
    tools_dir = "tools"
    file_path = os.path.join(tools_dir, f"{tool_name}.py")
    
    try:
        # 1. Write the code to the tools folder
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        
        # 2. Dynamically import to verify syntax
        spec = importlib.util.spec_from_file_location(tool_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        return ServiceResponse(
            status=ServiceResponse.SUCCESS, 
            content=f"SUCCESS: Tool '{tool_name}' created and verified. Agents can now use it via import."
        )
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Tool creation failed: {str(e)}")
