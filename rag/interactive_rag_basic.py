from simple_rag_basic import SimpleRAGBasic

def interactive_rag():
    """Interactive RAG system for real-time question answering"""
    
    print("Initializing Simple RAG System (TF-IDF version)...")
    print("="*50)
    
    # Initialize RAG system
    rag = SimpleRAGBasic()
    
    # Sample documents
    sample_documents = [
        "Python is a high-level programming language known for its simplicity and readability.",
        "Machine learning is a subset of artificial intelligence that enables computers to learn without being explicitly programmed.",
        "RAG (Retrieval-Augmented Generation) combines information retrieval with text generation to provide more accurate and contextual responses.",
        "Vector databases store and retrieve data using vector embeddings, enabling semantic search capabilities.",
        "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and human language.",
        "Deep learning uses neural networks with multiple layers to model and understand complex patterns in data.",
        "The transformer architecture revolutionized natural language processing with its attention mechanism.",
        "Embeddings are numerical representations of text that capture semantic meaning and relationships.",
        "FAISS is a library for efficient similarity search and clustering of dense vectors.",
        "Sentence transformers are models that convert text into meaningful vector representations.",
        "TF-IDF is a statistical measure that evaluates how important a word is to a document in a collection.",
        "Cosine similarity measures the cosine of the angle between two vectors, indicating their similarity."
    ]
    
    # Add documents and build index
    print("Adding documents to knowledge base...")
    rag.add_documents(sample_documents)
    
    print("Building search index...")
    rag.build_index()
    
    print("\nRAG System Ready!")
    print("="*50)
    print("You can now ask questions. Type 'quit' to exit.")
    print("="*50)
    
    while True:
        try:
            # Get user input
            query = input("\nEnter your question: ").strip()
            
            # Check for quit command
            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not query:
                print("Please enter a question.")
                continue
            
            # Generate response
            print("\nSearching for relevant information...")
            response = rag.generate_response(query)
            
            print("\n" + "="*50)
            print("RESPONSE:")
            print("="*50)
            print(response)
            print("="*50)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")

if __name__ == "__main__":
    interactive_rag()
