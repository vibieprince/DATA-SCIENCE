from langchain.tools import tool

@tool
def greet(name):
    """Generates a greeting message for the user"""
    return f"Hello {name}, Welcome to the AI world"

result = greet.invoke({"name":"Prince"})
print(result)
print(greet.name)
print(greet.description)
print(greet.args)