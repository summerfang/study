from rag_with_rl_rewards import RAGWithRL, RewardFunction

def interactive_rag_rl():
    """Interactive RAG system with RL reward evaluation"""
    
    print("Initializing RAG System with Reinforcement Learning Rewards...")
    print("="*60)
    
    # Initialize RAG system with RL
    rag = RAGWithRL()
    
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
        "Cosine similarity measures the cosine of the angle between two vectors, indicating their similarity.",
        "Reinforcement learning uses rewards to train agents to make optimal decisions in environments.",
        "Reward functions in RL provide feedback signals that guide the learning process toward desired behaviors."
    ]
    
    # Add documents and build index
    print("Adding documents to knowledge base...")
    rag.add_documents(sample_documents)
    
    print("Building search index...")
    rag.build_index()
    
    print("\nRAG System with RL Ready!")
    print("="*60)
    print("Available commands:")
    print("- Ask questions normally")
    print("- Type 'strategy:basic' for basic responses")
    print("- Type 'strategy:detailed' for detailed responses")
    print("- Type 'strategy:concise' for concise responses")
    print("- Type 'stats' to see performance statistics")
    print("- Type 'quit' to exit")
    print("="*60)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter your question or command: ").strip()
            
            # Check for quit command
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                print("Please enter a question or command.")
                continue
            
            # Check for stats command
            if user_input.lower() == 'stats':
                print("\n" + "="*50)
                print("PERFORMANCE STATISTICS")
                print("="*50)
                stats = rag.get_performance_stats()
                for key, value in stats.items():
                    if key == 'strategy_performance':
                        print(f"\n{key}:")
                        for strategy, perf in value.items():
                            print(f"  {strategy}: {perf}")
                    else:
                        print(f"{key}: {value}")
                continue
            
            # Check for strategy commands
            strategy = 'basic'  # default
            query = user_input
            
            if user_input.lower().startswith('strategy:'):
                parts = user_input.split(':', 1)
                if len(parts) == 2:
                    strategy = parts[0].replace('strategy:', '').strip()
                    query = parts[1].strip()
                    
                    if strategy not in ['basic', 'detailed', 'concise']:
                        print(f"Unknown strategy: {strategy}. Using 'basic' instead.")
                        strategy = 'basic'
            
            # Generate response with RL evaluation
            print(f"\nGenerating response using '{strategy}' strategy...")
            result = rag.generate_response(query, strategy=strategy)
            
            # Display results
            print("\n" + "="*60)
            print("RESPONSE & EVALUATION")
            print("="*60)
            print(f"Query: {result['query']}")
            print(f"Strategy: {result['strategy']}")
            print(f"Retrieved Documents: {len(result['retrieved_docs'])}")
            print("\n" + "-" * 40)
            print("RESPONSE:")
            print("-" * 40)
            print(result['response'])
            print("\n" + "-" * 40)
            print("REWARD EVALUATION:")
            print("-" * 40)
            print(f"Overall Reward: {result['reward_scores']['overall_reward']:.3f}")
            print(f"  - Relevance: {result['reward_scores']['relevance']:.3f}")
            print(f"  - Completeness: {result['reward_scores']['completeness']:.3f}")
            print(f"  - Clarity: {result['reward_scores']['clarity']:.3f}")
            print(f"  - Length: {result['reward_scores']['length']:.3f}")
            
            # Show reward weights
            print(f"\nReward Weights:")
            for component, weight in result['reward_scores']['weights'].items():
                print(f"  - {component}: {weight}")
            
            print("="*60)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")
    
    # Save history before exiting
    print("\nSaving response history...")
    rag.save_history()

if __name__ == "__main__":
    interactive_rag_rl()
