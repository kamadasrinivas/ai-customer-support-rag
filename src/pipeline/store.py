"""
SQLite Experiment Tracking.
This module manages the persistence layer for all evaluation runs. It establishes
a connection to a local SQLite database to log inputs, outputs, judge scores,
model configurations, and latency metrics for every single evaluation.

Classes:
- ExperimentTracker: Manages DB connections and table schemas.

Methods:
- log_run(config, metrics): Inserts a new experiment run.
- log_evaluation_case(run_id, query, response, score): Logs individual test case results.
- export_to_csv(): Dumps DB contents for external analysis.
"""

import asyncio

from rag.document_loader import DocumentLoaderFactory
from pathlib import Path

class DocumentIngestionPipeline:
    """Pipeline for ingesting documents into the SQLite experiment tracking database."""

    def __init__(self):
        print("Initializing Document Ingestion Pipeline...")
        
    def ingest_file(self, file_path: str):
        """Ingest a single document file into the database."""
        file_type = file_path.split('.')[-1].lower()
        loader = DocumentLoaderFactory.get_loader(file_type)
        if loader:
            content = asyncio.run(loader.load(file_path))
            # Here you would typically insert the content into the database
            print(f"Ingested content from {file_path}: {content[:100]}...")  # Print first 100 chars
        else:
            print(f"No loader available for file type: {file_type}")

    async def ingest_directory(self, directory_path: str):
        """Ingest all documents from a directory."""
        for file_path in Path(directory_path).glob("*"):
            if file_path.is_file():
                self.ingest_file(str(file_path))

async def main():
    """Main entry point for the document ingestion pipeline."""
    pipeline = DocumentIngestionPipeline()
    pipeline.ingest_file(r"C:\SRINI\IITM\CAPSTONEPROJECT\ai-customer-support-rag\data\test\hr_policies.txt")  # Example usage; replace with actual file paths
    # Here you would typically call methods to ingest documents
    # For example: await pipeline.ingest_documents()
    
if __name__ == "__main__":
    asyncio.run(main())