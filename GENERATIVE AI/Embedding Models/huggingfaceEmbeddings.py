from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# text = "This is a test document."
texts = [
    "Hello this is Prince Singh",
    "Hello your name is You Tube",
    "And you all are very beautiful"
]
# query_result = embeddings.embed_query(text)
query_result = embeddings.embed_documents(texts)

print(query_result)