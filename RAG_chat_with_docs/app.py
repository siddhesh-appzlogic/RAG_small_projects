import os
from pydoc import doc
from dotenv import load_dotenv
import chromadb
from openai import OpenAI
from chromadb.utils import embedding_functions
from pydantic import DirectoryPath

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_api_key,model_name="text-embedding-3-small"
)

# initialize chroma client with persistenance
chroma_client = chromadb.PersistentClient(path="chroma_persistent_storage")
collection_name = "document_qa_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name,embedding_function=openai_ef  # type: ignore
)
 
client = OpenAI(api_key=openai_api_key)

# resp = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role":"system","content":"You are a helpful assistant that can answer questions about the document."},
#         {"role":"user","content":"What is the life expectancy of a human in india?"}
#     ]
# )

# function to load documents from a directory
def load_documents_from_directory(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(directory_path,filename),'r',encoding='utf-8') as file:
                documents.append({"id":filename,"text":file.read()})
    return documents

# function to split text into chunks
def split_text(text,chunk_size=1000,chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks

# load documents from directory
directory_path = "./news_articles"
documents = load_documents_from_directory(directory_path)

print(f"Loaded {len(documents)} documents") 

# split documents into chunks
chunked_documents = []
for doc in documents:
    chunks = split_text(doc["text"])
    print("===splitting docs into chunks===")
    for i,chunk in enumerate(chunks):
        chunked_documents.append({"id":f"{doc['id']}_chunk{i+1}", "text":chunk})

# print(f"split documents into {len(chunked_documents)} chunks")

# function to generate embeddings using OpenAI API
def get_openai_embeddings(text):
    response = client.embeddings.create(input=text,model="text-embedding-3-small")
    embeddings = response.data[0].embedding
    print("===generating embeddings===")
    return embeddings

# generate embeddings for the document chunks
for doc in chunked_documents:
    print("=== Generating embeddings... ===")
    doc["embedding"] = get_openai_embeddings(doc["text"])

# print(doc["embedding"])

# Upsert documents with embeddings into chroma
for doc in chunked_documents:
    print("=== Inserting chunks into db ===")
    collection.upsert(ids=[doc["id"]],documents=[doc["text"]],embeddings=[doc["embedding"]])

# function to query the document
def query_documents(question,n_results=2):
    # query_embedding = get_openai_embeddings(question)
    results = collection.query(query_texts=[question],n_results=n_results)

    # extract the relevant chunks
    relevant_chunks = []
    if results["documents"]:
        relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
    print("=== Relevant chunks ===")
    return relevant_chunks

#function to generate a response from OpenAI
def generate_response(question,relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    prompt = (
        "You are an assistant for question-answering tasks. Use the following pieces of "
        "retrieved context to answer the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the answer concise."
        "\n\nContext:\n" + context + "\n\nQuestion:\n" + question
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"system",
                "content":prompt
            },
            {
                "role":"user",
                "content":question
            },
        ],
    )
    answer = response.choices[0].message
    return answer

#exmple query
# question = "tell me about AI replacing tv writers jobs"
question = "tell me about databricks"
relevant_chunks = query_documents(question)
answer = generate_response(question,relevant_chunks)
print("=== Answer ===")
print(answer)


