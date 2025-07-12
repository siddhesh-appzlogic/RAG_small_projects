# Document Q&A using OpenAI + ChromaDB (RAG Pipeline)

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to query a collection of documents and receive context-aware answers. It combines document chunking, semantic embedding with OpenAI, persistent storage using ChromaDB, and natural language response generation via GPT-3.5.

## Features

- Automatically loads and processes `.txt` documents from a directory
- Splits documents into manageable chunks
- Generates embeddings using OpenAI's `text-embedding-3-small model`
- Stores and queries document chunks using `ChromaDB` with persistent storage
- Generates answers using `GPT-3.5-turbo` by incorporating relevant context chunks

## Project Structure

- **`main.py`** - Core RAG pipeline implementation: loads, chunks, embeds, stores, queries, and generates answers.

- **`./news_articles/`** - Directory containing `.txt` files that serve as the source documents for question answering.

- **`.env`** - Stores your OpenAI API key as `OPENAI_API_KEY`. Required for embedding and chat models.

- **`chroma_persistent_storage/`** - Folder automatically created by ChromaDB to persist the vector store.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key**
Create a `.env` file:
   
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Required packages:**
- `openai`
- `chromadb`
- `python-dotenv`
- `pydantic`


4. **Prepare Documents**
Place `.txt` files you want to query in the `./news_articles/` directory.

## How It Works
**🔸 Step-by-step Pipeline** 

1. **Document Loading**
All `.txt` files in the specified directory are loaded.

2. **Chunking**
Each document is split into overlapping text chunks (default: 1000 characters with 20-character overlap).

3. **Embedding**
Each chunk is embedded using OpenAI’s embedding model (`text-embedding-3-small`).

4. **Storage in ChromaDB**
The chunks and their embeddings are stored in a **persistent ChromaDB collection**.

5. **Querying**
When a user asks a question, the top relevant chunks are retrieved based on semantic similarity.

6. **Answer Generation**
Retrieved chunks are used as context to generate a concise response with `gpt-3.5-turbo`.

## Example
```bash
question = "Tell me about Databricks"
relevant_chunks = query_documents(question)
answer = generate_response(question, relevant_chunks)
print(answer)
```

## Sample Output
```bash
=== Answer ===
Databricks is a data and AI company known for its unified data analytics platform built on Apache Spark. It enables data engineering, collaborative data science, and machine learning at scale. The platform is used across industries for real-time data processing and predictive analytics.
```

## Notes
- Document chunks are stored persistently in `chroma_persistent_storage/` for reuse across sessions.

- Embedding generation may incur OpenAI API usage costs.

- This implementation is suitable for `.txt` documents. You can extend it to support `.pdf` or `.docx`.

## Future Improvements
- PDF document support
- Web UI using Streamlit or Flask
- Query rewriting and multi-query expansion
- Feedback loop for answer relevance

## ⭐️ If you find this helpful, please give the repo a star!


### 🔧 Installation & Usage- Clone the repository:
git clone https://github.com/siddhesh-appzlogic/RAG_small_projects.git

## 🏷️ License
This project is licensed under the MIT License.

## 🧑‍💻 Author

**Mr. Siddhesh Walunj**  
GitHub: [https://github.com/SiddheshWalunj](https://github.com/siddhesh-appzlogic)

## 🤝 Contributions
Feel free to contribute by submitting pull requests or suggesting improvements!