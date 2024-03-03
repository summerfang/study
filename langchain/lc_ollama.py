from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

output = llm.invoke("how can langsmith help with testing?")

print(output)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "What is the best LLM")
])

chain = prompt | llm 

output = chain.invoke({"input": "how can langsmith help with testing?"})

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

output = chain.invoke({"input": "how can langsmith help with testing?"})
print(output)
