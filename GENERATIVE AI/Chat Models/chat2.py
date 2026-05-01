from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None, # 20 tokens
    timeout=None,
    max_retries=2,
    # other params...
)

response = model.invoke("Write a poem on AI.")

print(response.content)