# Document Intelligence with Query Expansion and Embedding Visualization

This project demonstrates how to use modern NLP techniques—including Dense Passage Retrieval (DPR), OpenAI GPT, ChromaDB, and UMAP—for document question answering, query expansion, and embedding analysis.

## Features

- 🔍 **Dense Passage Retrieval (DPR)** for semantic search
- 🧠 **Query expansion** using OpenAI's GPT models
- 📄 **Document ingestion** from PDF reports
- 📊 **UMAP visualization** of query-document relationships
- ⚡ **Vector database** with ChromaDB and SentenceTransformers

## Project Structure

- **`dpr_technique.py`** – Implements a basic Dense Passage Retrieval (DPR) pipeline using Hugging Face’s pre-trained DPR models. It encodes a user query and multiple candidate passages into dense embeddings, computes cosine similarity, and returns the most relevant result. Useful for standalone semantic retrieval.

- **`expansion_answer.py`** – Enhances a user query with a hypothetical answer generated via OpenAI’s GPT models. The original and augmented queries are embedded and used to retrieve relevant chunks from an annual report (PDF) stored in ChromaDB. UMAP is used for visualizing semantic relationships in the embedding space.

- **`expansion_queries.py`** – Generates multiple semantically related sub-questions from an original query using GPT-3.5. These sub-queries help retrieve a broader and deeper set of document chunks from ChromaDB. It deduplicates results and visualizes the semantic spread using UMAP for insightful query coverage.

- **`helper_utils.py`** – Contains utility functions for:
   - Projecting embeddings using UMAP.
   - Wrapping long text for readability.
   - Extracting text from PDF files.
   - Creating and populating a ChromaDB collection with document embeddings.This module centralizes common operations for reuse across different components.

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

3. **Place your PDF document**
Place the target PDF (e.g., an annual report) in the `data/`  directory.

4. **Usage**
Run each script as needed:

```bash
python dpr_technique.py
python expansion_answer.py
python expansion_queries.py
python reranking.py
```
5. **Requirements**
Python 3.8+

`transformers`, `chromadb`, `openai`, `langchain`, `umap-learn`, `pypdf`, `matplotlib`

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
