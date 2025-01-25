# XmasWishes Projekt - README

## Projektübersicht
Dieses Projekt implementiert einen Prototyp für ein XmasWishes-System, das in zwei Teilen entwickelt wurde:

1. **Aufgabe 3:** Implementierung eines REST-APIs mit Flask, das Wünsche speichert und verwaltet. Es enthält eine Lasttest-Simulation und unterstützt eine skalierbare Bereitstellung mit Docker.
2. **Aufgabe 4:** Integration eines Apache-Camel-Prozesses zur Verarbeitung eingescannten Wunschzettel-Dateien und deren Übertragung in das XmasWishes-System.

## Anforderungen und Umsetzung

### Aufgabe 3: REST-API mit Flask
#### Anforderungen:
- Ein einfaches REST-API für Lese- und Schreibzugriffe.
- Simulation von Lasttests zur Ermittlung der maximalen API-Calls pro Sekunde.
- Einsatz von Docker zur Unterstützung von Skalierbarkeit.

#### Umsetzung:
- **API-Endpunkte:**
  - `GET /wishes`: Gibt alle gespeicherten Wünsche aus.
  - `POST /wishes`: Fügt einen neuen Wunsch hinzu. Der Wunschtext wird im JSON-Format gesendet.
  - `PUT /wishes/<id>`: Aktualisiert den Status eines bestehenden Wunsches. Erwartet ein JSON mit dem neuen Status (z. B. `{"status": 2}`).

- **Docker-Integration:**
  - Eine `Dockerfile` wurde erstellt, um die Flask-Anwendung in einem Container bereitzustellen.
  - Ermöglicht die einfache Bereitstellung und Skalierbarkeit durch Containerisierung.

- **Lasttest:**
  - Die Datei `load_test.py` simuliert parallele Lese- und Schreibzugriffe auf die API.
  - Es werden mehrere Threads verwendet, um die maximale Anzahl von Requests pro Sekunde zu ermitteln.

### Aufgabe 4: Apache Camel Integration
#### Anforderungen:
- Verarbeitung von eingescannten Wunschzetteln, die als `.txt`-Dateien in einem Ordner gespeichert werden.
- Automatische Übertragung der Wunschdaten an das XmasWishes-System.

#### Umsetzung:
- **CamelRoute:**
  - Liest Dateien aus dem Ordner `scanned`.
  - Extrahiert den Inhalt der `.txt`-Dateien und erstellt eine JSON-Nachricht mit dem Wunschtext und einem Standardstatus.
  - Überträgt die Nachricht per HTTP `POST` an die XmasWishes-API.

- **Ordnerstruktur:**
  - Der Ordner `scanned` dient als Eingabeverzeichnis für eingescannten Wunschzettel.

- **Ablauf:**
  - Eine Datei wird in den Ordner `scanned` gelegt.
  - Apache Camel erkennt die Datei, liest den Inhalt und sendet den Wunsch als JSON an das XmasWishes-System.

## Projektstruktur
```
XMAS_PROTOTYPE/
├── app.py             # REST-API Implementierung
├── load_test.py       # Lasttest-Skript
├── Dockerfile         # Docker-Konfiguration
├── camel_integration/ # Apache Camel Anwendung
│   ├── src/main/java/org/example/
│   │   ├── CamelMain.java
│   │   └── CamelRoute.java
│   └── pom.xml       # Maven Konfigurationsdatei
├── scanned/           # Ordner für eingescannten Wunschzettel
└── ...
```

## Installation und Ausführung

### 1. Flask REST-API starten
1. Erstelle eine virtuelle Umgebung und installiere die Abhängigkeiten:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Starte die Anwendung:
   ```bash
   python app.py
   ```
3. Die API ist erreichbar unter: [http://localhost:7887](http://localhost:7887)

### 2. Docker verwenden
1. Baue das Docker-Image:
   ```bash
   docker build -t xmas_prototype .
   ```
2. Starte den Container:
   ```bash
   docker run -p 7887:7887 xmas_prototype
   ```

### 3. Apache Camel starten
1. Gehe in das Verzeichnis `camel_integration`:
   ```bash
   cd camel_integration
   ```
2. Baue die Anwendung mit Maven:
   ```bash
   mvn clean package
   ```
3. Starte die Camel-Anwendung:
   ```bash
   java -jar target/camel-integration-1.0.0-jar-with-dependencies.jar
   ```

### 4. Lasttest ausführen
1. Stelle sicher, dass die Flask-API läuft.
2. Führe das Lasttest-Skript aus:
   ```bash
   python load_test.py
   ```

## Nutzung
- **API:**
  - `GET /wishes`: Liste aller Wünsche abrufen.
  - `POST /wishes`: Wunsch hinzufügen. Beispiel:
    ```json
    {
        "wish": "Ich wünsche mir ein Fahrrad",
        "status": 1
    }
    ```
  - `PUT /wishes/<id>`: Status eines Wunsches aktualisieren. Beispiel:
    ```json
    {
        "status": 2
    }
    ```

- **Camel Integration:**
  - Lege eine `.txt`-Datei in den Ordner `scanned`.
  - Der Wunsch wird automatisch verarbeitet und an die XmasWishes-API gesendet.

## Fazit
Dieses Projekt demonstriert die grundlegende Funktionsweise eines verteilten Systems zur Verwaltung von Weihnachtswünschen. Es kombiniert moderne Web-Technologien (Flask) mit Integrationslösungen (Apache Camel) und zeigt, wie skalierbare und flexible Lösungen entwickelt werden können.
