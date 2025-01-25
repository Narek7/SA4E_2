# Basis-Image: schlankes Python 3.12.6
FROM python:3.12.6-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Hier könnte man eine requirements.txt kopieren, falls vorhanden
# z.B.: COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Für diesen kleinen Prototyp reicht Flask in minimaler Version:
RUN pip install --no-cache-dir Flask==2.2.3 Werkzeug==2.3.7

# Kopiere die lokalen Dateien ins Image
COPY . .

# Flask-App läuft auf Port 7887
EXPOSE 7887

# Starte die Flask-App
CMD ["python", "app.py"]
