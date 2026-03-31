import os
import glob
from agentscope.service import ServiceResponse
from utils.executor import check_path_permission

# Global list of user-approved "External" paths for this session
APPROVED_PATHS = []

def write_to_file(file_path: str, content: str) -> ServiceResponse:
    """
    Writes content to a specific file. 
    Strictly restricted to workspace unless user approves otherwise.
    """
    is_allowed, detail = check_path_permission(file_path)
    
    if not is_allowed and file_path not in APPROVED_PATHS:
        return ServiceResponse(
            status=ServiceResponse.ERROR, 
            content=f"PERMISSION_DENIED: The path '{file_path}' is outside your workspace. "
                    f"You must ask the user for permission with details on WHY you need this access."
        )

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return ServiceResponse(status=ServiceResponse.SUCCESS, content=f"Successfully wrote to {file_path}")
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Failed to write file: {str(e)}")

def read_from_file(file_path: str) -> ServiceResponse:
    """
    Reads content from a specific file.
    Strictly restricted to workspace unless user approves otherwise.
    """
    is_allowed, detail = check_path_permission(file_path)
    
    if not is_allowed and file_path not in APPROVED_PATHS:
        return ServiceResponse(
            status=ServiceResponse.ERROR, 
            content=f"PERMISSION_DENIED: Cannot read '{file_path}'. It is outside the workspace sandbox."
        )

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return ServiceResponse(status=ServiceResponse.SUCCESS, content=content)
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Failed to read file: {str(e)}")

def list_workspace_files(directory: str) -> ServiceResponse:
    """
    Lists all files in a directory recursively.
    """
    is_allowed, detail = check_path_permission(directory)
    if not is_allowed and directory not in APPROVED_PATHS:
        return ServiceResponse(status=ServiceResponse.ERROR, content="PERMISSION_DENIED: Directory access restricted.")

    try:
        files = glob.glob(f"{directory}/**/*", recursive=True)
        files = [f for f in files if os.path.isfile(f)]
        return ServiceResponse(status=ServiceResponse.SUCCESS, content="\n".join(files))
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=f"Failed to list files: {str(e)}")
