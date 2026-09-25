"""
Embedding Model Wrappers.
This module acts as an abstraction layer over various embedding models (e.g., OpenAI's
text-embedding-ada-002, HuggingFace sentence-transformers, Cohere).
It provides a unified interface for converting text chunks into dense vector representations.
It also includes logic for batch processing, handling rate limits, and caching embeddings
to avoid redundant API calls and reduce costs during indexing.

Classes:
- BaseEmbeddingModel: Abstract base class for embedding models.
- OpenAIEmbeddings: Implementation for OpenAI API.
- HuggingFaceEmbeddings: Local embedding generation using sentence-transformers.

Functions:
- get_embedding(text): Returns the embedding vector for a single string.
- get_embeddings_batch(texts): Returns a list of vectors for a batch of strings.
"""

from abc import ABC, abstractmethod

class BaseEmbeddingModel(ABC):
    """Abstract base class for embedding models."""
    
    def __init__(self, model_name: str):
        pass
    
    @abstractmethod
    def get_embedding(self, chunk: str) :
        """Return the embedding vector for a single string."""
        pass
    
    @abstractmethod
    def get_embeddings_batch(self, texts: list):
        """Return a list of vectors for a batch of strings."""
        pass
    
class OpenAIEmbeddings(BaseEmbeddingModel):
    """Concrete implementation of BaseEmbeddingModel for OpenAI's embedding API."""
    
    def get_embedding(self, chunk: str):
        """Return the embedding vector for a single string using OpenAI API."""
        # Implementation for calling OpenAI API goes here
        pass
    
    def get_embeddings_batch(self, texts: list):
        """Return a list of vectors for a batch of strings using OpenAI API."""
        # Implementation for batch processing with OpenAI API goes here
        pass
    
    