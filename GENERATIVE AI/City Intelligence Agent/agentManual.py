from dotenv import load_dotenv
import os 
import requests
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage,ToolMessage
from tavily import TavilyClient
from rich import print

@tool
def getWeather(city:str)->str:
    """Get Current weather of a city"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    print("DEBUG : ",data)

    if data.get("cod") != 200:
        return f"Error : {data.get('message','Could not fetch weather')}"
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"Weather in {city} : {desc},{temp} C"


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool 
def getNews(city:str)->str:
    """Get latest news about a city"""
    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3
    )

    results = response.get("results",[])

    if not results:
        return f"No news found for {city}"
    
    news_list = []

    for r in results:
        title = r.get("title","No title")
        url = r.get("url","")
        snippet = r.get("content","")

        news_list.append(
            f"-{title}\n{url}\n{snippet[:100]}..."
        )

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)

llm = ChatMistralAI(model="mistral-small-latest")
tools = {
    "getWeather": getWeather,
    "getNews": getNews
}

llm_with_tools = llm.bind_tools([getWeather, getNews])

messages = []

print("City Intelligence Agent")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break 

    messages.append(HumanMessage(content=user_input))

    while True:
        result = llm_with_tools.invoke(messages)
        messages.append(result)

        if result.tool_calls:
            for tool_call in result.tool_calls:
                tool_name = tool_call["name"]

                confirm = input(f"\nAgent wants to call '{tool_name}'. Approval? (yes/no)")

                if confirm.lower() != "yes":
                    print("Tool call denied\n")
                    break

                tool_result = tools[tool_name].invoke(tool_call)

                messages.append(
                    ToolMessage(
                        content=tool_result,
                        tool_call_id = tool_call["id"]
                    )
                )
            
            continue

        else:
            print("Final Answer:\n")
            print(result.content)
            print("\n"+"="*50 + "\n")
            break

# User input -> LLM (decides tool) -> Tool executes -> Tool Message added -> Loop Again -> LLM(final answer)