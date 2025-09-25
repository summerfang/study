import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple

class SimpleRAGBasic:
    def __init__(self):
        """
        Initialize a simple RAG system using TF-IDF
        """
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.documents = []
        self.tfidf_matrix = None
        
    def add_documents(self, documents: List[str]):
        """
        Add documents to the knowledge base
        
        Args:
            documents: List of document texts
        """
        self.documents.extend(documents)
        print(f"Added {len(documents)} documents. Total documents: {len(self.documents)}")
        
    def build_index(self):
        """Build the TF-IDF index for document retrieval"""
        if not self.documents:
            raise ValueError("No documents to index!")
            
        # Create TF-IDF matrix for all documents
        print("Creating TF-IDF matrix...")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
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
        if self.tfidf_matrix is None:
            raise ValueError("Index not built! Call build_index() first.")
            
        # Transform the query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        
        # Get top k indices
        top_indices = similarities.argsort()[-k:][::-1]
        
        # Return documents with their scores
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:  # Only return documents with some similarity
                results.append((self.documents[idx], float(similarities[idx])))
                
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
        
        # Simple response generation
        response = f"Based on the retrieved information:\n\n"
        
        for i, (doc, score) in enumerate(retrieved_docs, 1):
            response += f"Document {i} (relevance: {score:.3f}):\n{doc}\n\n"
            
        response += f"Query: {query}\n"
        response += f"Retrieved {len(retrieved_docs)} relevant documents."
        
        return response

def main():
    """Example usage of the SimpleRAG system"""
    
    # Initialize RAG system
    rag = SimpleRAGBasic()
    
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
