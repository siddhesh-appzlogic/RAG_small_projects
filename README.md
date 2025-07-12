## Combined two Small Projects in RAG (Retrieval-augmented generation)

This repository contains two separate RAG-based (Retrieval-Augmented Generation) implementations:

1. **RAG\_chat\_with\_docs**
   This project is a simple RAG chatbot that allows users to ask questions based on the content of custom documents (like PDFs or text files). It uses `LangChain`, OpenAI's GPT model, and `ChromaDB` for vector storage and retrieval. Key components include document loaders, chunking, embeddings, and a persistent vector store. You can query the stored knowledge through a conversational interface. It’s a great starting point to understand how to use vector databases in combination with LLMs.

2. **Advance\_RAG\_Techniques**
   This folder showcases more advanced RAG methods. It includes improvements in retrieval strategies (like hybrid search or metadata filtering), better prompt engineering, and a more modular and maintainable codebase. It’s designed for those who already understand the basics of RAG and want to build scalable, production-ready applications.

**Use Cases**:

* AI-powered document Q\&A systems
* Knowledge assistants
* Research tools

**Technologies Used**:

* `Python`
* `LangChain`
* `OpenAI GPT APIs`
* `ChromaDB`
* `Git LFS (for large file storage)`

**Notes**:

* Sensitive files like `.env` should be excluded from Git history (done).
* Large binaries (e.g., ChromaDB data files) are managed using Git LFS.
