from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env (if needed for other purposes)
load_dotenv()

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic you want")

# Ollama LLAMA2 LLM
llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Check if input text exists and process it
if input_text:
    st.write(chain.invoke({"question": input_text}))
