# Base image
FROM python:3.9

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copiar arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock ./

# Instalar o Poetry e as dependências
RUN pip install poetry && poetry install --no-root

# Copiar o restante do código do projeto
COPY . .

# Comando principal: executar o main.py com o Poetry
CMD ["poetry", "run", "python", "scraper_project/main.py"]