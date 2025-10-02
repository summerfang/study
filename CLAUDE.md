# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal learning and experimentation repository covering multiple programming languages, frameworks, and technologies. The owner uses this for hands-on learning and creating small code snippets to understand various technologies. The directory structure is organized by technology/framework name, with each containing isolated learning projects.

## Key Directory Structure

### Languages
- **python/**: Data science, ML experiments, algorithms, basic scripts
  - `datascience/`: pandas, matplotlib examples
  - `algorithm/`: algorithm implementations
  - Multiple standalone learning scripts

- **javascript/**: Core JavaScript concepts (promises, async, modules, regex)
  - `modules/`: Module pattern examples (IIFE, ES6 modules)
  - `promise/`: Promise implementations
  - `regex/`: Regular expression patterns

- **typescript/**: TypeScript learning projects
  - `hw/`: Main TypeScript project with axios, XMLHttpRequest examples

- **node/**: Node.js server examples, filesystem ops, events, websockets
  - `websocket/`: WebSocket server/client examples
  - `api/`: Basic API implementations

- **c/** and **cplusplus/**: C/C++ examples, data types, algorithms

- **go/**: Go language basics with custom packages

- **java/**: Java fundamentals

### Frameworks & Libraries

- **react/**: React apps with routing, components
  - `my-third-react-app/`: React Router examples
  - `s1/`: Basic React setup

- **reactnative/**: React Native/Expo projects
  - `StickerSmash/`, `my-app/`: Expo-based mobile apps
  - `google-auth/`: Authentication examples

- **nextjs/**: Next.js with SSG, API routes
  - Posts/pages architecture using file-based routing

- **remix/**: Remix framework projects
  - `my-second-remix-app/`: Remix with data loaders

- **vue/**: Vue.js learning projects

- **langchain/**: LangChain + Ollama integration
  - RAG implementations with FAISS
  - Chat history, embeddings, retrieval chains

- **openai/**: OpenAI API integration
  - `audio/`: Audio transcription
  - `embeddings/`: Embedding creation
  - `chat/`: Chat completion examples

### Data Science & ML

- **cnn/**: Convolutional Neural Networks with Keras/TensorFlow
  - CIFAR-10 training examples
  - Saliency maps, feature maps
  - CNN architecture implementations

- **ml/**: Machine learning experiments
  - Ridge/Lasso regression
  - SVM implementations
  - `learn_keras_001/`: Keras DNN examples

- **leetcode/**: Algorithm practice
  - `matrix/`: Matrix manipulation problems
  - `math/`: Mathematical algorithms
  - `beginner/`: Entry-level problems

### DevOps & Tools

- **docker/**: Docker examples with Python, Node.js apps

- **vscodeextension/**: VS Code extension development
  - `hw/`, `helloworld/`: Extension boilerplates

- **electron-webpack/**, **eletronjs/**: Electron desktop apps

- **ffmpeg/**: Video processing scripts
  - `many_videos/`: Video layout strategies, multi-video compositions

## Common Development Patterns

### Running Python Scripts
Most Python scripts are standalone and can be run directly:
```bash
python path/to/script.py
```

For ML/CNN projects, dependencies may include:
- keras, tensorflow
- pandas, numpy, matplotlib
- scikit-learn

### Running Node.js Projects
Simple Node.js scripts:
```bash
node path/to/script.js
```

Projects with package.json (like `node/`):
```bash
npm start
```

### Running TypeScript Projects
TypeScript projects typically use:
```bash
npm install
npm run build  # or tsc
node dist/output.js
```

### React/Next.js Projects
Standard React/Next.js workflow:
```bash
npm install
npm run dev     # Development server
npm run build   # Production build
```

### VS Code Extensions
For extension development (in `vscodeextension/`):
```bash
npm install
# Press F5 in VS Code to launch Extension Development Host
```

## Important Conventions

1. **Isolated Learning Projects**: Each subdirectory is independent - don't expect shared dependencies or monorepo structure

2. **Experimentation Over Production**: Code quality varies as this is a learning repository. Focus on understanding concepts rather than production-ready implementations

3. **Minimal Documentation**: Most projects lack README files. Infer purpose from code structure and filenames

4. **Technology Proficiency Levels**: The owner categorizes their knowledge as: Heard it → Knew it → Learned it → Used it → Mastered it (see main README.md)

5. **Azure Functions**: `.vscode/tasks.json` shows Azure Functions configuration for Python projects under `azure/funcTest`

## Working in This Repository

- When exploring a technology area, start by examining the most recently modified files
- Standalone scripts typically have `if __name__ == '__main__':` blocks (Python) or direct execution patterns
- Look for `package.json`, `requirements.txt`, or similar dependency files to understand project setup
- Many projects are "hello world" style - expect simple, educational examples rather than complex applications
