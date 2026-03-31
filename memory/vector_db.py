import os
import glob
from agentscope.service import ServiceResponse

def init_vector_db():
    try:
        import chromadb
        client = chromadb.PersistentClient(path="./runs/chroma_db")
        return client
    except ImportError:
        return None

def index_workspace(project_name: str):
    """Reads all files in a workspace and adds them to the vector DB."""
    client = init_vector_db()
    if not client:
        return "ChromaDB not installed. Skipping indexing."
        
    collection = client.get_or_create_collection(name=f"proj_{project_name}")
    workspace_dir = os.path.join("workspace", project_name)
    
    files = glob.glob(f"{workspace_dir}/**/*", recursive=True)
    
    docs = []
    ids = []
    metadatas = []
    
    for i, filepath in enumerate(files):
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Chunking could be added here for large files
                    docs.append(content)
                    ids.append(f"doc_{i}")
                    metadatas.append({"path": filepath})
            except UnicodeDecodeError:
                pass # Skip binary
                
    if docs:
        collection.upsert(documents=docs, ids=ids, metadatas=metadatas)
        return f"Indexed {len(docs)} files."
    return "No files to index."

def log_lesson_learned(agent_name: str, lesson: str):
    """Saves a 'lesson learned' to a global store shared by all projects."""
    client = init_vector_db()
    if not client: return
    collection = client.get_or_create_collection(name="global_knowledge")
    import uuid
    collection.add(
        documents=[lesson],
        ids=[str(uuid.uuid4())],
        metadatas=[{"agent": agent_name, "type": "lesson"}]
    )

def query_global_knowledge(query: str) -> str:
    """Queries the global knowledge base for relevant history."""
    client = init_vector_db()
    if not client: return ""
    try:
        collection = client.get_collection(name="global_knowledge")
        results = collection.query(query_texts=[query], n_results=2)
        if not results['documents'][0]: return ""
        return "\n".join(results['documents'][0])
    except:
        return ""

def query_codebase(query: str, project_name: str = "default") -> ServiceResponse:
    """Semantic search tool for the Coder to find relevant files."""
    client = init_vector_db()
    if not client:
        return ServiceResponse(status=ServiceResponse.ERROR, content="ChromaDB not installed.")
        
    try:
        collection = client.get_collection(name=f"proj_{project_name}")
        results = collection.query(query_texts=[query], n_results=3)
        
        if not results['documents'][0]:
            return ServiceResponse(status=ServiceResponse.SUCCESS, content="No relevant code found.")
            
        context = ""
        for i, doc in enumerate(results['documents'][0]):
            path = results['metadatas'][0][i]['path']
            context += f"\n--- FILE: {path} ---\n{doc[:1000]}...\n"
            
        return ServiceResponse(status=ServiceResponse.SUCCESS, content=context)
    except Exception as e:
        return ServiceResponse(status=ServiceResponse.ERROR, content=str(e))
