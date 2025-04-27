# Lektion-2

## Einführung
In dieser Lektion werden wir uns mit der Verwendung der `ChatPromptTemplate`-Klasse
aus dem `langchain_core.prompts`-Modul beschäftigen. Diese Klasse ermöglicht es uns,
Vorlagen für Prompts zu erstellen, die wir an das LLM-Modell senden können.
Wir werden verschiedene Methoden zur Erstellung von Prompts untersuchen und sehen,
wie wir diese in unserer Anwendung nutzen können. 🚀✨

### 1. Importieren der Klasse
Zuerst müssen wir die `ChatPromptTemplate`-Klasse importieren:

```python
from langchain_core.prompts import ChatPromptTemplate
```

### 2. Erstellen einer Prompt-Vorlage
Wir können eine Prompt-Vorlage erstellen, indem wir die Methode `from_template` verwenden. Hier ist ein Beispiel, das einen Witz über ein bestimmtes Thema erzählt:

```python
prompt_template = ChatPromptTemplate.from_template("Erzähl mir einen Witz über ein {tema}")
```

### 3. Aufruf der Prompt-Vorlage
Um die Vorlage zu verwenden, rufen wir die `invoke`-Methode auf und übergeben die erforderlichen Parameter:

```python
prompt = prompt_template.invoke({"tema": "Kamele"})
```

### 4. Verwendung von Nachrichten-Templates
Wir können auch Vorlagen für Nachrichten erstellen, um den Kontext der Interaktion zu steuern. Hier ist ein Beispiel:

```python
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","Reagiert auf den Nutzer als Pirat, mit Emojis, wenn der Kontext es zulässt."),
        ("human", "{input}")
    ]
)
```

### 5. Erstellen einer Kette von Vorlagen
Wir können auch eine Kette von Vorlagen erstellen, um die Interaktion zu steuern:

```python
chain = prompt_template | llm
response = chain.invoke({"tema": "Kamele"})
print(response.content)
```

Viel Spaß beim Experimentieren mit der `ChatPromptTemplate`-Klasse! 🎉🎈
