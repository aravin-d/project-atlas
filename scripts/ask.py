import chromadb
import ollama

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("lms_docs")

question = input("Question: ")

# Step 1 - Convert question to embedding
embedding_response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

query_embedding = embedding_response["embeddings"][0]

# Step 2 - Search Chroma
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

context = "\n\n".join(results["documents"][0])

# Step 3 - Build prompt
prompt = f"""
You are an LMS documentation assistant.

Answer ONLY using the provided context.

If the answer is not in the context, say:
'I could not find that information in the documentation.'

Context:
{context}

Question:
{question}
"""

# Step 4 - Ask Qwen
response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nANSWER\n")
print(response["message"]["content"])
