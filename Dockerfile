# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código da aplicação para o diretório de trabalho
COPY . .

# Cria o diretório para o banco de dados SQLite
RUN mkdir -p dados

# Expõe a porta em que a aplicação será executada
EXPOSE 5000

# Define a variável de ambiente para o Flask
ENV FLASK_APP=info_pet.py

# Comando para executar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]