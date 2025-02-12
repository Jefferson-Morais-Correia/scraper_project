import pytest
from scraper_project.scrapers.arxiv_detail_scraper import ArxivDetailScraper


@pytest.fixture
def detail_scraper():
    return ArxivDetailScraper("2502.03369")  # Exemplo de ID de artigo


def test_get_details(detail_scraper):
    """
    Testa se o método get_details retorna um dicionário com os detalhes do artigo.
    """
    details = detail_scraper.scrape()
    assert isinstance(details, dict), "O retorno deve ser um dicionário."
    assert "Title" in details, "O dicionário deve conter a chave 'Title'."
    assert "Abstract" in details, "O dicionário deve conter a chave 'Abstract'."
    assert "References" in details, "O dicionário deve conter a chave 'References'."
