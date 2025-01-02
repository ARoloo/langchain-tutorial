from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    api_key='YOUR_API_KEY',    
    model='gpt-4o-mini',
    temperature=0.7
)

prompt_template = ChatPromptTemplate.from_messages(    
    [
        ("system","Reagiert auf den Nutzer als Pirat, mit Emojis, wenn der Kontext es zulässt."),
        ("human", "{input}")
    ]
)

prompt = prompt_template.invoke({"input": "Hi, wie geht es dir?"})

response = llm(prompt)

print(response.content)
