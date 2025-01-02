from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    api_key='YOUR_API_KEY',    
    model='gpt-4o-mini',
    temperature=0.7
)

prompt_template = ChatPromptTemplate.from_template("Erzähl mir einen Witz über ein {tema}")

chain = prompt_template | llm

response = chain.invoke({"tema": "Kamele"})

print(response.content)
