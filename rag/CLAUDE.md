# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview

This is a Retrieval-Augmented Generation (RAG) system implementation with multiple versions:

1. **Basic Version (TF-IDF based)**: Uses scikit-learn TF-IDF vectorization and cosine similarity
2. **Advanced Version (Embeddings based)**: Uses sentence-transformers with FAISS indexing
3. **RL-Enhanced Version**: Includes reinforcement learning reward functions to evaluate response quality

### Core Components

- **SimpleRAGBasic** (`simple_rag_basic.py`): TF-IDF implementation using `TfidfVectorizer`
- **SimpleRAG** (`simple_rag.py`): Sentence transformer implementation using FAISS indexing
- **RewardFunction** (`rag_with_rl_rewards.py`): Multi-component reward evaluation system with relevance, completeness, clarity, and length scoring
- Interactive versions available for all implementations

## Development Commands

### Dependencies

**Basic Version (minimal)**:
```bash
pip install scikit-learn numpy
```

**Advanced Version (full features)**:
```bash
pip install -r requirements.txt
```

### Running the System

**Basic TF-IDF version**:
```bash
python simple_rag_basic.py
python interactive_rag_basic.py  # Interactive mode
```

**Advanced embedding version**:
```bash
python simple_rag.py
python interactive_rag.py  # Interactive mode
```

**RL-enhanced version**:
```bash
python rag_with_rl_rewards.py
python interactive_rag_rl.py  # Interactive mode
```

## Key Design Patterns

- **Document ingestion**: All classes use `add_documents()` followed by `build_index()`
- **Retrieval**: `retrieve(query, k)` returns list of (document, score) tuples
- **Response generation**: Template-based responses using retrieved context
- **Reward evaluation**: Multi-dimensional scoring with configurable weights

## Testing Queries

The system includes built-in test queries:
- "What is Python?"
- "How does machine learning work?"
- "What is RAG?"
- "Tell me about vector databases"