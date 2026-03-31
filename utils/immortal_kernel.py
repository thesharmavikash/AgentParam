import json
import os
import shutil
import zipfile
from datetime import datetime

class ImmortalKernel:
    """Handles the serialization and resurrection of the AI Organization."""
    def __init__(self, company_name):
        self.company_name = company_name
        self.company_path = f"companies/{company_name}"
        self.genome_dir = "shared_library/genomes"
        os.makedirs(self.genome_dir, exist_ok=True)

    def create_genome(self):
        """Freezes the entire company state into a single 'Genome' package."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        genome_name = f"{self.company_name}_genome_{timestamp}.zip"
        genome_path = os.path.join(self.genome_dir, genome_name)
        
        print(f"🧬 [ImmortalKernel] Synthesizing Genome: {genome_name}...")
        
        # Package the company directory (ledger, kpis, knowledge graph, projects)
        with zipfile.ZipFile(genome_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.company_path):
                for file in files:
                    zipf.write(os.path.join(root, file), 
                               os.path.relpath(os.path.join(root, file), 
                               os.path.join(self.company_path, '..')))
        
        return genome_path

    def resurrect_from_genome(self, genome_path):
        """Restores a company's entire consciousness from a genome file."""
        print(f"🕯️ [ImmortalKernel] Initiating Resurrection from: {genome_path}")
        with zipfile.ZipFile(genome_path, 'r') as zipf:
            zipf.extractall(".")
        return True
