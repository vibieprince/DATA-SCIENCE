import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

# Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
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

# UI
st.set_page_config(page_title="Movie Info Extractor", layout="centered")

st.title("🎬 Movie Information Extractor")

para = st.text_area("Enter your paragraph:", height=200)

if st.button("Extract Information"):
    if para.strip() == "":
        st.warning("Please enter a paragraph.")
    else:
        with st.spinner("Processing..."):
            final_prompt = prompt.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            })

            response = model.invoke(final_prompt)

            try:
                movie_data = parser.parse(response.content)

                st.success("Extraction Complete!")

                st.subheader("📌 Extracted Data")
                st.write(movie_data)

            except Exception as e:
                st.error("Failed to parse response.")
                st.text("Raw Output:")
                st.code(response.content)