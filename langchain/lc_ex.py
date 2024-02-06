from langchain_core.prompts import ChatPromptTemplate

from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])