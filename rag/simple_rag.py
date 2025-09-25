import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from typing import List, Dict, Tuple
import json

class SimpleRAG:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize a simple RAG system
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.embeddings = None
        self.index = None
        
    def add_documents(self, documents: List[str]):
        """
        Add documents to the knowledge base
        
        Args:
            documents: List of document texts
        """
        self.documents.extend(documents)
        print(f"Added {len(documents)} documents. Total documents: {len(self.documents)}")
        
    def build_index(self):
        """Build the FAISS index for document retrieval"""
        if not self.documents:
            raise ValueError("No documents to index!")
            
        # Create embeddings for all documents
        print("Creating embeddings...")
        self.embeddings = self.model.encode(self.documents, show_progress_bar=True)
        
        # Initialize FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        
        # Add embeddings to index
        self.index.add(self.embeddings.astype('float32'))
        print(f"Index built with {len(self.documents)} documents")
        
    def retrieve(self, query: str, k: int = 3) -> List[Tuple[str, float]]:
        """
        Retrieve the most relevant documents for a query
        
        Args:
            query: The search query
            k: Number of documents to retrieve
            
        Returns:
            List of tuples (document, similarity_score)
        """
        if self.index is None:
            raise ValueError("Index not built! Call build_index() first.")
            
        # Encode the query
        query_embedding = self.model.encode([query])
        
        # Search the index
        scores, indices = self.index.search(query_embedding.astype('float32'), k)
        
        # Return documents with their scores
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx < len(self.documents):  # Ensure index is valid
                results.append((self.documents[idx], float(score)))
                
        return results
    
    def generate_response(self, query: str, k: int = 3) -> str:
        """
        Generate a response based on retrieved documents
        
        Args:
            query: The user query
            k: Number of documents to retrieve
            
        Returns:
            Generated response
        """
        # Retrieve relevant documents
        retrieved_docs = self.retrieve(query, k)
        
        if not retrieved_docs:
            return "I couldn't find any relevant information to answer your question."
        
        # Simple response generation (in a real system, you'd use an LLM here)
        response = f"Based on the retrieved information:\n\n"
        
        for i, (doc, score) in enumerate(retrieved_docs, 1):
            response += f"Document {i} (relevance: {score:.3f}):\n{doc}\n\n"
            
        response += f"Query: {query}\n"
        response += f"Retrieved {len(retrieved_docs)} relevant documents."
        
        return response

def main():
    """Example usage of the SimpleRAG system"""
    
    # Initialize RAG system
    rag = SimpleRAG()
    
    # Sample documents (in a real system, these would come from your knowledge base)
    sample_documents = [
        "Python is a high-level programming language known for its simplicity and readability.",
        "Machine learning is a subset of artificial intelligence that enables computers to learn without being explicitly programmed.",
        "RAG (Retrieval-Augmented Generation) combines information retrieval with text generation to provide more accurate and contextual responses.",
        "Vector databases store and retrieve data using vector embeddings, enabling semantic search capabilities.",
        "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and human language.",
        "Deep learning uses neural networks with multiple layers to model and understand complex patterns in data.",
        "The transformer architecture revolutionized natural language processing with its attention mechanism.",
        "Embeddings are numerical representations of text that capture semantic meaning and relationships."
    ]
    
    # Add documents to the knowledge base
    print("Adding documents to knowledge base...")
    rag.add_documents(sample_documents)
    
    # Build the search index
    print("Building search index...")
    rag.build_index()
    
    # Example queries
    test_queries = [
        "What is Python?",
        "How does machine learning work?",
        "What is RAG?",
        "Tell me about vector databases"
    ]
    
    # Test the system
    print("\n" + "="*50)
    print("TESTING THE RAG SYSTEM")
    print("="*50)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 30)
        response = rag.generate_response(query)
        print(response)
        print("\n" + "="*50)

if __name__ == "__main__":
    main()
