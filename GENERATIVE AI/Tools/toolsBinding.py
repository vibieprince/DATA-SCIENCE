from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print 
load_dotenv()

@tool
def getLength(text:str)->int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "getLength":getLength
}

llm = ChatMistralAI(model="mistral-small-latest")

# tool binding
llm_with_tool = llm.bind_tools([getLength])

message = []
prompt = input("You : ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)

result = llm_with_tool.invoke(message)
print(result.content)
