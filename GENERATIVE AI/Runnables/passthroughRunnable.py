from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatMistralAI(model="mistral-small-latest")
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a code generator"),
    ("human","{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant who explains code in simple terms"),
    ("human","Explain the following code in simple words:\n{code}")
])

seq = code_prompt | model | parser

wrap = RunnableLambda(lambda x: {"code": x})

seq2 = RunnableParallel(
    {
        "code": lambda x: x["code"],
        "explaination": explain_prompt | model | parser
    }
)

chain = seq | wrap | seq2

result = chain.invoke({
    "topic":"Write a code of string palindrome in python"
})

print(result['code'])
print(result['explaination'])