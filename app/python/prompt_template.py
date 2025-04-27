import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv('API_KEY'),
    model=os.getenv('MODEL'),
    temperature=0.7
)

prompt_template = ChatPromptTemplate.from_template("Erzähl mir einen Witz über ein {tema}")

prompt = prompt_template.invoke({"tema": "Kamele"})

response = llm(prompt)

print(response.content)
