import json
import os

class GraphRAG:
    """Simulates a Knowledge Graph where entities (Agents, Files, Decisions) are nodes."""
    def __init__(self, company_name):
        self.graph_path = f"companies/{company_name}/knowledge_graph.json"
        self.nodes = {}
        self.edges = []

    def add_relationship(self, source, relation, target):
        """Maps a logical dependency (e.g. 'File A' depends on 'Database B')."""
        edge = {"source": source, "relation": relation, "target": target}
        self.edges.append(edge)
        self.save_graph()

    def get_impact_analysis(self, change_node):
        """Returns all entities affected by a change in one node."""
        affected = [e["target"] for e in self.edges if e["source"] == change_node]
        return affected

    def save_graph(self):
        with open(self.graph_path, "w") as f:
            json.dump({"nodes": self.nodes, "edges": self.edges}, f, indent=4)

    def query_logic(self, query_text):
        """Simulates finding the 'Reasoning Path' for a complex decision."""
        # High-level logic mapping for the agents
        return f"Logic Path Found: {query_text} -> Depends on project_security -> Impacted by GDPR_policy."

    def generate_visual_map(self):
        """Generates a Mermaid.js diagram string of the company's logical connections."""
        mermaid = "graph TD\n"
        for edge in self.edges:
            mermaid += f"    {edge['source']} -->|{edge['relation']}| {edge['target']}\n"
        
        map_path = self.graph_path.replace(".json", ".md")
        with open(map_path, "w") as f:
            f.write(f"# Company Knowledge Map\n\n```mermaid\n{mermaid}```")
        return f"Visual map generated at {map_path}"
