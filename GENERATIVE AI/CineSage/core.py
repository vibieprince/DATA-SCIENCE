from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert information extraction assistant.

Your task is to extract structured information from the given paragraph.

Instructions:
- Extract only relevant details
- Do not hallucinate
- If any field is missing, return null
- Fix minor spelling mistakes in names if obvious
- Follow the output format strictly

{format_instructions}
"""),

    ("human", """
Extract information from the following paragraph:

{paragraph}
""")
])

para = input("Give your paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})

response = model.invoke(final_prompt)

movie_data = parser.parse(response.content)

print("\n✅ Extracted Data:\n")
print(movie_data)