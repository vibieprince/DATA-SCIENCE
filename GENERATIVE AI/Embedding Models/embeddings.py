from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

texts = [
    "Hello this is Prince Singh",
    "Hello your name is You Tube",
    "And you all are very beautiful"
]
# vector = embeddings.embed_query("You are going to learn Generative AI.") 
vector = embeddings.embed_documents(texts)
print(vector)