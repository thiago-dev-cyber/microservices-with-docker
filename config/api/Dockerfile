# Usa a imagem base do Python 3.9 slim
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo requirements.txt da raiz do projeto para o diretório /app no container
COPY ../../../ /app

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# (Opcional) Comando padrão para executar quando o container iniciar
CMD ["python", "./src/api.py"]