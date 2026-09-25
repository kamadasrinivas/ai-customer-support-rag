from abc import ABC, abstractmethod
import asyncio


class BaseDocumentLoader(ABC):
    """Abstract base class for document loaders."""
    def __init__(self, source: str):
        pass
    
    @abstractmethod
    async def load(self):
        """Load documents from a source."""
        pass
    
class TextLoader(BaseDocumentLoader):
    """Concrete implementation of BaseDocumentLoader for loading text documents."""

    async def load(self, path) -> str:
        """Load text documents from the specified source."""
        # Implementation for loading text documents goes here
        loop = asyncio.get_event_loop()
        def read_file():
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
            
        return await loop.run_in_executor(None, read_file)
    
    
class MarkdownLoader(BaseDocumentLoader):
    """Concrete implementation of BaseDocumentLoader for loading markdown documents."""

    async def load(self, path) -> str:
        """Load markdown documents from the specified source."""
        # Implementation for loading markdown documents goes here
        loop = asyncio.get_event_loop()
        def read_file():
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
            
        return await loop.run_in_executor(None, read_file) 
    
    
class PDFLoader(BaseDocumentLoader):
    """Concrete implementation of BaseDocumentLoader for loading PDF documents."""

    async def load(self, path) -> str:
        """Load PDF documents from the specified source."""
        # Implementation for loading PDF documents goes here
        loop = asyncio.get_event_loop()
        def read_pdf():
            import PyPDF2
            with open(path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
            
        return await loop.run_in_executor(None, read_pdf)
        
        
class DocumentLoaderFactory:
    """Factory class for creating document loaders based on file type."""

    @staticmethod
    def get_loader(file_type: str) -> BaseDocumentLoader:
        """Return the appropriate document loader based on the file type."""
        if file_type == "text":
            return TextLoader(source="")
        elif file_type == "markdown":
            return MarkdownLoader(source="")
        elif file_type == "pdf":
            return PDFLoader(source="")
        else:
            raise ValueError(f"Unsupported file type: {file_type}") 