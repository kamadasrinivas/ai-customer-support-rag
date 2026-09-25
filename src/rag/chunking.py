"""
Text Splitting and Chunking Strategies.
This file contains algorithms for breaking down large documents into smaller, semantically
meaningful chunks before embedding. It includes implementations for:
- Recursive Character Text Splitting: Splitting by paragraphs, sentences, and words.
- Semantic Chunking: Grouping text based on embedding similarity to maintain context.
- Token-based Splitting: Ensuring chunks fit strictly within LLM context windows.
Proper chunking is critical for effective retrieval and minimizing noise in the context.

Functions:
- chunk_by_characters(text, chunk_size, overlap): Recursive splitting.
- chunk_by_tokens(text, max_tokens): Token-aware splitting.
- semantic_chunk(text, embedding_model): Groups sentences by semantic similarity.
"""

from abc import ABC, abstractmethod

class BaseChunker(ABC):
    """Abstract base class for text chunking strategies."""
    
    @abstractmethod
    def chunk(self, text: str):
        """Chunk the input text into smaller segments."""
        pass
    
class SlidingWindowChunker(BaseChunker):
    """Concrete implementation of BaseChunker using a sliding window approach."""
    
    def __init__(self, chunk_size: int=1000, overlap: int=200):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk(self, text: str):
        """Chunk the input text using a sliding window."""
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(text[start:end])
            start += self.chunk_size - self.overlap
        return chunks
       
class SectionBasedChunker(BaseChunker):
    """Concrete implementation of BaseChunker that splits text by sections."""
    
    def chunk(self, text: str):
        """Chunk the input text by splitting on section headers."""
        import re
        # Split on common section headers (e.g., "##", "###", etc.)
        sections = re.split(r'\n#+\s+', text)
        return [section.strip() for section in sections if section.strip()]
    