# Lektion-1

## Einleitung
Herzlich willkommen! 😊 In dieser Datei erfahren Sie, wie Sie ein LLM-Modell (Large Language Model) mithilfe der `ChatOpenAI`-Klasse aus dem `langchain_openai`-Modul effektiv nutzen können. Diese Anleitung führt Sie durch die notwendigen Schritte, um die Bibliothek zu importieren, das Modell zu instanziieren und Anfragen zu senden. Außerdem lernen Sie, wie Sie Streaming- und Batch-Anfragen verwenden können. 🚀✨

### 1. Importieren der Bibliothek
Zuerst müssen wir die `ChatOpenAI`-Klasse aus dem `langchain_openai`-Modul importieren. Diese Klasse fungiert als Wrapper für die OpenAI-API und ermöglicht die Interaktion mit den Modellen von OpenAI.

```python
from langchain_openai import ChatOpenAI
```

### 2. Instanziierung des Modells
Nun erstellen wir ein Objekt `llm`, indem wir die `ChatOpenAI`-Klasse instanziieren. Hierbei müssen Sie Ihren API-Schlüssel, das Modell und die Temperatur angeben, um auf die OpenAI-Dienste zugreifen zu können. 🔑🌟

```python
llm = ChatOpenAI(
    api_key='YOUR_API_KEY',
    model='gpt-4o-mini',
    temperature=0.7
)
```

### 3. Aufruf des Modells
Um eine Anfrage an das Modell zu senden, verwenden wir die Methode `invoke`. Hierbei übergeben wir einen Textprompt, auf den das Modell reagieren soll. Die Antwort wird in der Variablen `response` gespeichert. 💬🤖

```python
response = llm.invoke("Hi, wie geht es dir?")
print(response.content)
```

### 4. Streaming von Antworten
Die Methode `stream` ermöglicht es uns, die Antwort des Modells in Echtzeit zu empfangen. Anstatt die gesamte Antwort auf einmal zu erhalten, wird die Antwort in Teilen (Chunks) zurückgegeben. Dies ist besonders nützlich, wenn die Antwort lang ist oder wenn Sie eine sofortige Rückmeldung wünschen. ⏳📦

```python
for chunk in llm.stream("Was soll ich lernen um eine ki experte zu werden?"):
    print(chunk.content, end="", flush=True)
```

### 5. Batch-Anfragen
Mit der Methode `batch` können Sie mehrere Prompts gleichzeitig senden und die Antworten in einer Liste erhalten. Dies ist effizient, wenn Sie mehrere Anfragen in einem einzigen Aufruf verarbeiten möchten. 📊📬

```python
responses = llm.batch(["Hi, wie geht es dir?", "Was soll ich lernen um eine ki expert zu wreden?"])
for response in responses:
    print(response.content)
```

### 6. Ausgabe der Antwort
Schließlich geben wir den Inhalt der Antwort, die das Modell zurückgibt, aus. Dies geschieht durch den Zugriff auf die `content`-Eigenschaft des `response`-Objekts. 📝✨

```python
print(response.content)
```

Viel Spaß beim Experimentieren mit dem LLM-Modell! 🎉🎈
