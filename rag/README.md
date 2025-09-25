# Simple RAG Example

This is a basic implementation of a Retrieval-Augmented Generation (RAG) system that demonstrates the core concepts of RAG:

1. **Document Storage**: Store your knowledge base documents
2. **Vector Generation**: Convert text to vectors using TF-IDF (basic version) or sentence transformers (advanced version)
3. **Similarity Search**: Use cosine similarity for document retrieval
4. **Response Generation**: Generate responses based on retrieved documents

## Features

- Simple and easy to understand implementation
- Two versions available:
  - **Basic version**: Uses TF-IDF and scikit-learn (works immediately)
  - **Advanced version**: Uses sentence-transformers and FAISS (requires additional setup)
- Includes sample documents and test queries
- No external API dependencies

## Installation

### Basic Version (Recommended to start)
The basic version works with minimal dependencies:

```bash
pip install scikit-learn numpy
```

### Advanced Version
For the advanced version with sentence transformers:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Version (TF-IDF based)
Run the basic example:
```bash
python simple_rag_basic.py
```

Or use the interactive version:
```bash
python interactive_rag_basic.py
```

### Advanced Version (Sentence Transformers)
Run the advanced example:
```bash
python simple_rag.py
```

Or use the interactive version:
```bash
python interactive_rag.py
```

## How it Works

### Basic Version (TF-IDF)
1. **Document Ingestion**: Documents are added to the knowledge base
2. **Indexing**: Documents are converted to TF-IDF vectors
3. **Query Processing**: User queries are converted to TF-IDF vectors
4. **Retrieval**: The most similar documents are retrieved using cosine similarity
5. **Response Generation**: A response is generated based on the retrieved documents

### Advanced Version (Sentence Transformers)
1. **Document Ingestion**: Documents are added to the knowledge base
2. **Indexing**: Documents are converted to embeddings and stored in a FAISS index
3. **Query Processing**: User queries are converted to embeddings
4. **Retrieval**: The most similar documents are retrieved using vector similarity
5. **Response Generation**: A response is generated based on the retrieved documents

## Customization

You can easily customize this system by:

- Adding your own documents to the `sample_documents` list
- Changing the embedding model in the `SimpleRAG` constructor
- Modifying the response generation logic
- Adding more sophisticated retrieval strategies

## Example Output

The system will demonstrate retrieval for queries like:
- "What is Python?"
- "How does machine learning work?"
- "What is RAG?"
- "Tell me about vector databases"

## Advanced Features

### Reinforcement Learning with Reward Functions

The system includes an advanced version with RL reward functions to evaluate prompt output quality:

```bash
# Run the RL-enhanced version
python rag_with_rl_rewards.py

# Interactive RL version
python interactive_rag_rl.py
```

**Key Features:**
- **Multi-component reward evaluation**: Relevance, completeness, clarity, and length
- **Strategy comparison**: Test different response generation strategies
- **Performance tracking**: Monitor and analyze response quality over time
- **Customizable weights**: Adjust importance of different quality dimensions

**Reward Components:**
- **Relevance**: How well the response addresses the query
- **Completeness**: How much information is covered
- **Clarity**: How well-structured and readable the response is
- **Length**: Whether the response is appropriately sized

## Next Steps

To enhance this simple RAG system, you could:

1. Add a proper LLM (like GPT) for response generation
2. Implement document chunking for better retrieval
3. Add document metadata and filtering
4. Implement caching for better performance
5. Add a web interface for easy interaction
6. **Enhance reward functions** with more sophisticated metrics
7. **Implement online learning** to improve rewards based on user feedback
