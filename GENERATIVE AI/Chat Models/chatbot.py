from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

chat_history = [
    SystemMessage(content="You are a funny AI agent.")
]
print("Welcome, type 0 to exit the application")

while(True):
    prompt = input("You : ")
    chat_history.append(HumanMessage(content=prompt))

    if prompt == '0':
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

