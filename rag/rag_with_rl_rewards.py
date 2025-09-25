import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Dict, Any
import json
import re
from datetime import datetime

class RewardFunction:
    """Base class for reward functions to evaluate prompt output quality"""
    
    def __init__(self, weights: Dict[str, float] = None):
        """
        Initialize reward function with component weights
        
        Args:
            weights: Dictionary of weights for different reward components
        """
        self.weights = weights or {
            'relevance': 0.4,
            'completeness': 0.3,
            'clarity': 0.2,
            'length': 0.1
        }
    
    def calculate_relevance_score(self, query: str, response: str, retrieved_docs: List[Tuple[str, float]]) -> float:
        """Calculate relevance score based on query-response alignment"""
        # Simple keyword matching
        query_words = set(query.lower().split())
        response_words = set(response.lower().split())
        
        # Calculate word overlap
        overlap = len(query_words.intersection(response_words))
        total_query_words = len(query_words)
        
        if total_query_words == 0:
            return 0.0
        
        return min(1.0, overlap / total_query_words)
    
    def calculate_completeness_score(self, response: str, retrieved_docs: List[Tuple[str, float]]) -> float:
        """Calculate completeness score based on information coverage"""
        if not retrieved_docs:
            return 0.0
        
        # Count unique information points in response
        response_sentences = [s.strip() for s in response.split('.') if s.strip()]
        
        # Simple heuristic: more sentences = more complete (up to a point)
        optimal_sentences = min(len(retrieved_docs) * 2, 5)  # 2 sentences per doc, max 5
        actual_sentences = len(response_sentences)
        
        if actual_sentences == 0:
            return 0.0
        
        # Penalize too few or too many sentences
        if actual_sentences < optimal_sentences:
            return actual_sentences / optimal_sentences
        else:
            return max(0.0, 1.0 - (actual_sentences - optimal_sentences) / optimal_sentences)
    
    def calculate_clarity_score(self, response: str) -> float:
        """Calculate clarity score based on response structure and readability"""
        if not response:
            return 0.0
        
        # Check for proper sentence structure
        sentences = [s.strip() for s in response.split('.') if s.strip()]
        if not sentences:
            return 0.0
        
        # Calculate average sentence length (prefer medium length)
        avg_length = np.mean([len(s.split()) for s in sentences])
        
        # Optimal sentence length is between 10-20 words
        if 10 <= avg_length <= 20:
            clarity_score = 1.0
        elif avg_length < 5:
            clarity_score = 0.3
        elif avg_length > 30:
            clarity_score = 0.5
        else:
            clarity_score = 0.7
        
        # Bonus for having structure indicators
        structure_indicators = ['first', 'second', 'third', 'additionally', 'furthermore', 'however']
        has_structure = any(indicator in response.lower() for indicator in structure_indicators)
        
        if has_structure:
            clarity_score = min(1.0, clarity_score + 0.2)
        
        return clarity_score
    
    def calculate_length_score(self, response: str) -> float:
        """Calculate length appropriateness score"""
        word_count = len(response.split())
        
        # Optimal length: 50-150 words
        if 50 <= word_count <= 150:
            return 1.0
        elif word_count < 20:
            return 0.2
        elif word_count > 300:
            return 0.3
        else:
            return 0.7
    
    def calculate_reward(self, query: str, response: str, retrieved_docs: List[Tuple[str, float]]) -> Dict[str, float]:
        """
        Calculate overall reward and component scores
        
        Returns:
            Dictionary with overall reward and component scores
        """
        relevance = self.calculate_relevance_score(query, response, retrieved_docs)
        completeness = self.calculate_completeness_score(response, retrieved_docs)
        clarity = self.calculate_clarity_score(response)
        length = self.calculate_length_score(response)
        
        # Calculate weighted reward
        overall_reward = (
            self.weights['relevance'] * relevance +
            self.weights['completeness'] * completeness +
            self.weights['clarity'] * clarity +
            self.weights['length'] * length
        )
        
        return {
            'overall_reward': overall_reward,
            'relevance': relevance,
            'completeness': completeness,
            'clarity': clarity,
            'length': length,
            'weights': self.weights
        }

class RAGWithRL:
    """RAG system with reinforcement learning reward evaluation"""
    
    def __init__(self, reward_function: RewardFunction = None):
        """
        Initialize RAG system with RL capabilities
        
        Args:
            reward_function: Custom reward function (optional)
        """
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.documents = []
        self.tfidf_matrix = None
        self.reward_function = reward_function or RewardFunction()
        self.response_history = []
        
    def add_documents(self, documents: List[str]):
        """Add documents to the knowledge base"""
        self.documents.extend(documents)
        print(f"Added {len(documents)} documents. Total documents: {len(self.documents)}")
        
    def build_index(self):
        """Build the TF-IDF index for document retrieval"""
        if not self.documents:
            raise ValueError("No documents to index!")
            
        print("Creating TF-IDF matrix...")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        print(f"Index built with {len(self.documents)} documents")
        
    def retrieve(self, query: str, k: int = 3) -> List[Tuple[str, float]]:
        """Retrieve relevant documents"""
        if self.tfidf_matrix is None:
            raise ValueError("Index not built! Call build_index() first.")
            
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:
                results.append((self.documents[idx], float(similarities[idx])))
                
        return results
    
    def generate_response(self, query: str, k: int = 3, strategy: str = 'basic') -> Dict[str, Any]:
        """
        Generate response with different strategies and evaluate quality
        
        Args:
            query: User query
            k: Number of documents to retrieve
            strategy: Response generation strategy ('basic', 'detailed', 'concise')
            
        Returns:
            Dictionary with response and evaluation metrics
        """
        retrieved_docs = self.retrieve(query, k)
        
        if not retrieved_docs:
            response = "I couldn't find any relevant information to answer your question."
            reward_scores = self.reward_function.calculate_reward(query, response, [])
            return {
                'query': query,
                'response': response,
                'retrieved_docs': [],
                'reward_scores': reward_scores,
                'strategy': strategy
            }
        
        # Generate response based on strategy
        if strategy == 'basic':
            response = self._generate_basic_response(query, retrieved_docs)
        elif strategy == 'detailed':
            response = self._generate_detailed_response(query, retrieved_docs)
        elif strategy == 'concise':
            response = self._generate_concise_response(query, retrieved_docs)
        else:
            response = self._generate_basic_response(query, retrieved_docs)
        
        # Calculate reward scores
        reward_scores = self.reward_function.calculate_reward(query, response, retrieved_docs)
        
        # Store in history
        self.response_history.append({
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'response': response,
            'strategy': strategy,
            'reward_scores': reward_scores,
            'retrieved_docs_count': len(retrieved_docs)
        })
        
        return {
            'query': query,
            'response': response,
            'retrieved_docs': retrieved_docs,
            'reward_scores': reward_scores,
            'strategy': strategy
        }
    
    def _generate_basic_response(self, query: str, retrieved_docs: List[Tuple[str, float]]) -> str:
        """Generate basic response"""
        response = f"Based on the retrieved information:\n\n"
        
        for i, (doc, score) in enumerate(retrieved_docs, 1):
            response += f"Document {i} (relevance: {score:.3f}):\n{doc}\n\n"
            
        response += f"Query: {query}\n"
        response += f"Retrieved {len(retrieved_docs)} relevant documents."
        
        return response
    
    def _generate_detailed_response(self, query: str, retrieved_docs: List[Tuple[str, float]]) -> str:
        """Generate detailed response with more structure"""
        response = f"Here's a comprehensive answer to your question: '{query}'\n\n"
        
        # Group by relevance
        high_relevance = [doc for doc, score in retrieved_docs if score > 0.5]
        medium_relevance = [doc for doc, score in retrieved_docs if 0.2 <= score <= 0.5]
        
        if high_relevance:
            response += "Key Information:\n"
            for i, doc in enumerate(high_relevance, 1):
                response += f"{i}. {doc}\n"
            response += "\n"
        
        if medium_relevance:
            response += "Additional Context:\n"
            for i, doc in enumerate(medium_relevance, 1):
                response += f"{i}. {doc}\n"
            response += "\n"
        
        response += f"Summary: Based on {len(retrieved_docs)} relevant sources, this information should help answer your question about '{query}'."
        
        return response
    
    def _generate_concise_response(self, query: str, retrieved_docs: List[Tuple[str, float]]) -> str:
        """Generate concise response"""
        # Take the most relevant document and create a brief summary
        if not retrieved_docs:
            return "No relevant information found."
        
        best_doc, best_score = retrieved_docs[0]
        
        # Create a simple summary
        sentences = best_doc.split('.')
        if len(sentences) > 1:
            summary = sentences[0] + "."
        else:
            summary = best_doc
        
        response = f"Answer: {summary}\n\n"
        response += f"Source relevance: {best_score:.3f}"
        
        return response
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics from response history"""
        if not self.response_history:
            return {"message": "No response history available"}
        
        # Calculate average rewards
        avg_rewards = []
        strategy_rewards = {}
        
        for entry in self.response_history:
            reward = entry['reward_scores']['overall_reward']
            avg_rewards.append(reward)
            
            strategy = entry['strategy']
            if strategy not in strategy_rewards:
                strategy_rewards[strategy] = []
            strategy_rewards[strategy].append(reward)
        
        # Calculate statistics
        stats = {
            'total_queries': len(self.response_history),
            'average_reward': np.mean(avg_rewards),
            'best_reward': max(avg_rewards),
            'worst_reward': min(avg_rewards),
            'strategy_performance': {}
        }
        
        for strategy, rewards in strategy_rewards.items():
            stats['strategy_performance'][strategy] = {
                'count': len(rewards),
                'average_reward': np.mean(rewards),
                'best_reward': max(rewards)
            }
        
        return stats
    
    def save_history(self, filename: str = 'rag_response_history.json'):
        """Save response history to file"""
        with open(filename, 'w') as f:
            json.dump(self.response_history, f, indent=2)
        print(f"Response history saved to {filename}")

def main():
    """Example usage of RAG with RL reward evaluation"""
    
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
        "Embeddings are numerical representations of text that capture semantic meaning and relationships."
    ]
    
    # Add documents and build index
    print("Setting up RAG system...")
    rag.add_documents(sample_documents)
    rag.build_index()
    
    # Test queries with different strategies
    test_queries = [
        "What is Python?",
        "How does machine learning work?",
        "What is RAG?",
        "Tell me about vector databases"
    ]
    
    strategies = ['basic', 'detailed', 'concise']
    
    print("\n" + "="*60)
    print("TESTING RAG WITH REINFORCEMENT LEARNING REWARDS")
    print("="*60)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        
        # Test each strategy
        for strategy in strategies:
            result = rag.generate_response(query, strategy=strategy)
            
            print(f"\nStrategy: {strategy.upper()}")
            print(f"Response: {result['response'][:200]}...")
            print(f"Overall Reward: {result['reward_scores']['overall_reward']:.3f}")
            print(f"  - Relevance: {result['reward_scores']['relevance']:.3f}")
            print(f"  - Completeness: {result['reward_scores']['completeness']:.3f}")
            print(f"  - Clarity: {result['reward_scores']['clarity']:.3f}")
            print(f"  - Length: {result['reward_scores']['length']:.3f}")
        
        print("\n" + "="*60)
    
    # Show performance statistics
    print("\nPERFORMANCE STATISTICS:")
    print("-" * 30)
    stats = rag.get_performance_stats()
    for key, value in stats.items():
        if key == 'strategy_performance':
            print(f"\n{key}:")
            for strategy, perf in value.items():
                print(f"  {strategy}: {perf}")
        else:
            print(f"{key}: {value}")
    
    # Save history
    rag.save_history()

if __name__ == "__main__":
    main()
