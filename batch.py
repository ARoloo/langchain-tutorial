from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key='YOUR_API_KEY',
    model='gpt-4o-mini',
    temperature=0.7
)

responses = llm.batch(["Hi, wie geht es dir?", "Was soll ich lernen um eine ki expert zu wreden?"])
for response in responses:
    print(response.content)
