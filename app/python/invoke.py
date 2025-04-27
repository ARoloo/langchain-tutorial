import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    api_key=os.getenv('API_KEY'),
    model=os.getenv('MODEL'),
    temperature=0.7
)
response = llm.invoke("Hi, wie geht es dir?")
print(response.content)
