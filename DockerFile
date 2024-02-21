# Utiliser une image de base Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et les installer
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]
