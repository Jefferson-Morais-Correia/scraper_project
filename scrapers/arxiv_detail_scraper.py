from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class ArxivDetailScraper(BaseScraper):
    BASE_URL = "https://arxiv.org"

    def __init__(self, paper_id):
        super().__init__()
        self.paper_id = paper_id

    def scrape(self):
        paper_url = f"{self.BASE_URL}/html/{self.paper_id}"
        response = self.session.get(paper_url, verify=False)

        if response.status_code != 200:
            print(f"Erro: Não foi possível obter detalhes do paper ID {self.paper_id}. Código de status: {response.status_code}")
            return None  # Retorna antes de chegar no BeautifulSoup

        soup = BeautifulSoup(response.content, "html.parser")
        
        # Se chegou aqui, significa que response.status_code == 200
        title_tag = soup.find(class_="ltx_title")
        abstract_tag = soup.find(class_="ltx_abstract")
        bibliography_tag = soup.find(class_="ltx_bibliography")

        title = title_tag.text.strip() if title_tag else "Título não encontrado"
        abstract = abstract_tag.text.strip() if abstract_tag else "Resumo não encontrado"
        bibliography = bibliography_tag.text.strip() if bibliography_tag else "Bibliografia não encontrada"

        return {"Title": title, "Abstract": abstract, "References": bibliography}


