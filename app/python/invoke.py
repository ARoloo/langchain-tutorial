from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key='YOUR_API_KEY',
    model='gpt-4o-mini',
    temperature=0.7
)
response = llm.invoke("Hi, wie geht es dir?")
print(response.content)
