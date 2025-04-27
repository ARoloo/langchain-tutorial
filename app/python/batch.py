import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    api_key=os.getenv('API_KEY'),
    model=os.getenv('MODEL'),
    temperature=0.7
)

responses = llm.batch([
    "Hi, wie geht es dir?",
    "Was soll ich lernen, um ein KI-Experte zu werden?"
])
for response in responses:
    print(response.content)
