# Lektion-1

## Einleitung
Herzlich willkommen! 😊 In dieser Datei erfahren Sie, wie Sie ein LLM-Modell (Large Language Model) mithilfe der `MistalAi`-Klasse effektiv nutzen können. Diese Anleitung führt Sie durch die notwendigen Schritte, um die Bibliothek zu importieren, das Modell zu instanziieren und Anfragen zu senden. Außerdem lernen Sie, wie Sie Streaming- und Batch-Anfragen verwenden können. 🚀✨

### 1. Importieren der Bibliothek
Zuerst müssen wir die `ChatMistralAI`-Klasse importieren. Diese Klasse ermöglicht die Interaktion mit den Modellen von Mistal.

```python
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
```

### 2. Instanziierung des Modells
Zuerst laden wir die Umgebungsvariablen aus der `.env`-Datei und erstellen dann ein Objekt `llm`, indem wir die `ChatMistralAI`-Klasse instanziieren. Hierbei müssen Sie sicherstellen, dass die Umgebungsvariablen `API_KEY` und `MODEL` in Ihrer `.env`-Datei definiert sind. 🔑🌟

```python
load_dotenv()

llm = ChatMistralAI(
    api_key=os.getenv('API_KEY'),
    model=os.getenv('MODEL'),
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
for chunk in llm.stream("Was soll ich lernen, um ein KI-Experte zu werden?"):
    print(chunk.content, end="", flush=True)
```

### 5. Batch-Anfragen
Mit der Methode `batch` können Sie mehrere Prompts gleichzeitig senden und die Antworten in einer Liste erhalten. Dies ist effizient, wenn Sie mehrere Anfragen in einem einzigen Aufruf verarbeiten möchten. 📊📬

```python
responses = llm.batch(["Hi, wie geht es dir?", "Was soll ich lernen, um ein KI-Experte zu werden?"])
for response in responses:
    print(response.content)
```

### 6. Ausgabe der Antwort
Schließlich geben wir den Inhalt der Antwort, die das Modell zurückgibt, aus. Dies geschieht durch den Zugriff auf die `content`-Eigenschaft des `response`-Objekts. 📝✨

```python
print(response.content)
```

Viel Spaß beim Experimentieren mit dem LLM-Modell von Mistal! 🎉🎈
