# Scraper Project

**Versão atual:** 0.1.0

## Descrição do Projeto

Este projeto é um scraper que coleta informações do site [arXiv](https://arxiv.org/), incluindo IDs de artigos, títulos, resumos e referências bibliográficas. Ele foi desenvolvido em Python e utiliza bibliotecas como `requests`, `beautifulsoup4` e `pandas` para manipulação de dados e coleta de informações.

---

## Estrutura do Projeto

```bash
scraper_project/
├── scraper_project/             # Diretório principal do código
│   ├── __init__.py              # Inicialização do pacote
│   ├── main.py                  # Ponto de entrada principal do programa
│   ├── scrapers/                # Módulo para scrapers
│   │   ├── __init__.py          # Inicialização do módulo de scrapers
│   │   ├── base_scraper.py      # Classe base para scrapers (Singleton)
│   │   ├── arxiv_id_scraper.py  # Classe para pegar os IDs dos artigos
│   │   ├── arxiv_detail_scraper.py # Classe para pegar os detalhes de cada artigo
│   │   ├── scraper_factory.py   # Classe Factory para criar scrapers de detalhes
│   ├── utils/                   # Módulo para utilitários
│   │   ├── __init__.py          # Inicialização do módulo de utilitários
│   │   ├── helpers.py           # Funções auxiliares (ex.: salvar CSV)
│   │   ├── logging_config.py    # Configuração dos logs
├── tests/                       # Diretório para testes automatizados e unitários
│   ├── __init__.py              # Inicialização do módulo de testes
│   ├── test_arxiv_id_scraper.py # Testes para o scraper de IDs
│   ├── test_arxiv_detail_scraper.py # Testes para o scraper de detalhes
│   ├── test_scraper_factory.py  # Testes para a Factory
│   ├── test_main_flow.py        # Testes de integração para o fluxo principal
│   ├── test_utils.py            # Testes para funções utilitárias
├── .pre-commit-config.yaml      # Configuração para pre-commit hooks
├── .bumpversion.cfg             # Configuração para o bump2version
├── Dockerfile                   # Configuração do Docker para execução do projeto
├── Makefile                     # Automação de tarefas
├── pyproject.toml               # Configuração do Poetry e dependências
├── poetry.lock                  # Arquivo de lock do Poetry (gerado automaticamente)
├── README.md                    # Documentação do projeto
├── VERSION                      # Arquivo de controle de versão
├── LICENSE                      # Licença do projeto (opcional)


## Bibliotecas Utilizadas

As bibliotecas e suas versões utilizadas no projeto estão descritas no arquivo `pyproject.toml`. Aqui estão as principais:

### Dependências Principais:
- **Python**: >= 3.9
- **requests**: ^2.31.0
- **beautifulsoup4**: ^4.12.2
- **pandas**: >=1.4.0,<1.6.0
- **numpy**: >=1.21.0,<1.25.0

### Dependências de Desenvolvimento:
- **pytest**: ^7.4.2
- **ruff**: ^0.0.280
- **pre-commit**: ^3.4.0
- **bump2version**: ^1.0.1

---

## Requisitos de Instalação

1. **Python 3.9 ou superior**: Certifique-se de que o Python está instalado na sua máquina. Você pode verificar a versão com:
    ```bash
    python --version
    ```

2. **Poetry**: Gerenciador de dependências utilizado no projeto. Instale-o com:
    ```bash
    pip install poetry
    ```

3. **Docker (opcional)**: Para executar o projeto em um container Docker, é necessário ter o Docker instalado.

---

## Como Instalar

Após clonar o repositório, siga os passos abaixo para configurar o ambiente:

### 1. Clone o Repositório
```bash
git clone https://github.com/Jefferson-Morais-Correia/scraper_project.git
cd scraper_project


## Instale as Dependências

Com o Poetry instalado, execute o seguinte comando para instalar todas as dependências necessárias para o projeto:

```bash
poetry install
```

Isso instalará todas as dependências listadas no arquivo `pyproject.toml`.

---

## Como Executar o Projeto

### 1. Executar Localmente

Para rodar o projeto localmente, use o comando abaixo:

```bash
poetry run python scraper_project/main.py
```

### 2. Executar com Docker

Se preferir usar o Docker, siga os passos abaixo:

#### Construir o Container

```bash
docker build -t scraper_project .
```

#### Executar o Container

```bash
docker run --rm scraper_project
```

---

## Como Fazer Requisições

### Coleta de IDs dos Artigos

A classe `ArxivIdScraper` é responsável por coletar os IDs dos artigos mais recentes. Aqui está um exemplo de como utilizá-la:

```python
from scrapers.arxiv_id_scraper import ArxivIdScraper

id_scraper = ArxivIdScraper()
ids = id_scraper.scrape(skip=0, show=100)
print(ids)
```

### Coleta de Detalhes dos Artigos

A classe `ArxivDetailScraper` coleta detalhes como título, resumo e referências bibliográficas de um artigo específico. Exemplo:

```python
from scrapers.arxiv_detail_scraper import ArxivDetailScraper

scraper = ArxivDetailScraper("1234.56789")
details = scraper.scrape()
print(details)
```

### Fluxo Completo

O fluxo completo do scraping está implementado no arquivo `main.py`. Ele coleta IDs, busca detalhes dos artigos e salva os resultados em um arquivo CSV. Para executá-lo, use o comando abaixo:

```bash
poetry run python scraper_project/main.py
```

---

## Testes Automatizados

O projeto utiliza `pytest` para testes. Para executá-los, use o seguinte comando:

```bash
poetry run pytest tests/
```

---

## Automação com Makefile

O projeto inclui um arquivo `Makefile` para facilitar tarefas comuns. Aqui estão alguns exemplos de como utilizá-lo:

### Construir e rodar o Docker

```bash
make start
```

### Executar testes

```bash
make tests
```

### Verificar qualidade do código

```bash
make quality
```

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

Agora **todo o texto original foi convertido para Markdown**, com blocos de código (`bash` e `python`) corretamente formatados e títulos organizados. É só copiar e colar! 