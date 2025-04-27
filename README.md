# 📚 Einstieg in Langchain: Dein Wegweiser für KI-gestützte Projekte

## 🎉 Willkommen zu unserem Langchain-Tutorial!
In dieser Anleitung werden Sie die Grundlagen der Integration von KI-Technologien kennenlernen. Sie werden entdecken, wie Sie KI-Agenten effizient auf Ihrem eigenen Computer nutzen können, um Ihre Projekte zu bereichern. Diese App demonstriert die nahtlose Verwendung von leistungsstarken Sprachmodellen unter Wahrung Ihrer Datensicherheit und Privatsphäre. Lassen Sie uns gemeinsam die aufregende Welt der KI erkunden und lernen, wie Sie Ihre eigenen intelligenten Anwendungen entwickeln können!

## 📂 Inhaltsverzeichnis
- [Technologien](#technologien)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Ausführen von Python-Programmen im Container](#ausführen-von-python-programmen-im-container)

## 🛠️ Technologien
- **Langchain**: Ein Framework zur Entwicklung von Anwendungen, die von Sprachmodellen betrieben werden. Mehr dazu unter [Langchain](https://www.langchain.com/).
- **Mistral**: Ein Werkzeug zum Ausführen großer Sprachmodelle lokal. Besuchen Sie [Mistral](https://mistral.com) für weitere Informationen.
- **Docker**: Eine Plattform zur Automatisierung der Bereitstellung von Anwendungen in Containern. Erfahren Sie mehr über [Docker](https://www.docker.com/).

## 🌐 LLM-Modelle
In dieser Sektion werden verschiedene LLM-Modelle vorgestellt, die Sie verwenden können, darunter **ChatGPT** und **Ollama**. Diese Beispiele werden unter Verwendung der **Mistral API** erstellt. Sie können die leistungsstarken Sprachmodelle nutzen, um Ihre Projekte zu bereichern und innovative Lösungen zu entwickeln.

### Verfügbare Modelle:
- **ChatGPT**: Ein fortschrittliches KI-Modell, das natürliche Sprache versteht und erzeugt.
- **Ollama**: Ein weiteres KI-Modell, das sich durch seine Flexibilität und Anpassungsfähigkeit auszeichnet.

## Voraussetzungen
- [Docker Installationsanleitung](https://docs.docker.com/get-docker/)
- [Docker Compose Installationsanleitung](https://docs.docker.com/compose/install/)

## 🚀 Installation
Um diese Anwendung auszuführen, stellen Sie sicher, dass Sie Docker und Docker Compose installiert haben. Befolgen Sie die folgenden Schritte, um die Anwendung einzurichten:

### Schritt 1: Klonen des Git-Repositorys
Um das Repository zu klonen, verwenden Sie den folgenden Befehl in Ihrem Terminal:
```bash
 git clone <repository_url>
```
Dieser Befehl erstellt eine lokale Kopie des Repositorys auf Ihrem Computer. Stellen Sie sicher, dass Sie `<repository_url>` durch die tatsächliche URL des Repositorys ersetzen.

### Schritt 2: Navigieren Sie zum Projektverzeichnis
Nachdem Sie das Repository geklont haben, navigieren Sie in das Projektverzeichnis mit dem Befehl:
```bash
 cd <repository_directory>
```
Ersetzen Sie `<repository_directory>` durch den Namen des Ordners, der erstellt wurde, als Sie das Repository geklont haben. Dieser Ordner enthält alle notwendigen Dateien zum Ausführen der Anwendung.

### Schritt 3: Bauen und Ausführen der Anwendung
Sobald Sie im Projektverzeichnis sind, führen Sie den folgenden Befehl aus, um die Anwendung zu bauen und zu starten:
```bash
 docker-compose up -d --build
```
Dieser Befehl startet die Anwendung im Hintergrund und baut die notwendigen Docker-Container.

### Zugriff auf den Container
Um auf den Container zuzugreifen, verwenden Sie den folgenden Befehl:
```bash
docker exec -ti <container_name> bash
```
Ersetzen Sie `<container_name>` durch den tatsächlichen Namen Ihres Containers.

## Ausführen von Python-Programmen im Container
Sobald Sie Zugriff auf den Container haben, können Sie Python-Programme ausführen. Verwenden Sie den folgenden Befehl, um ein bestimmtes Python-Skript zu starten:
```bash
python filename.py
```
Ersetzen Sie 'filename.py' durch den Namen des Python-Skripts, das Sie ausführen möchten. Stellen Sie sicher, dass das Skript im aktuellen Verzeichnis vorhanden ist oder geben Sie den vollständigen Pfad an, um es erfolgreich zu starten.
