from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key='YOUR_API_KEY',
    model='gpt-4o-mini',
    temperature=0.7
)

for chunk in llm.stream("Was soll ich lernen um eine ki experte zu werden?"):
    print(chunk.content, end="", flush=True)
