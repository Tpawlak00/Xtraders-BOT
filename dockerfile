# Użyj oficjalnego obrazu Python jako bazowego
FROM python:3.10-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt .

# Zainstaluj wymagane pakiety
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj pozostałe pliki projektu do katalogu roboczego
COPY . .

# Wyłącz buforowanie wyjścia Pythona
ENV PYTHONUNBUFFERED=1

# Uruchom główny plik aplikacji przy starcie kontenera
CMD ["python", "main.py"]
