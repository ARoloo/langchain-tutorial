import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()  # Lädt die Umgebungsvariablen aus der .env-Datei

llm = ChatMistralAI(
    api_key=os.getenv('API_KEY'),
    model=os.getenv('MODEL'),
    temperature=0.7
)

for chunk in llm.stream("Was soll ich lernen, um ein KI-Experte zu werden?"):
    print(chunk.content, end="", flush=True)
