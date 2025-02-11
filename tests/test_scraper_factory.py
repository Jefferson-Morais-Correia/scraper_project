from scraper_project.scrapers.scraper_factory import ScraperFactory
from scraper_project.scrapers.arxiv_detail_scraper import ArxivDetailScraper


def test_factory_creates_scraper():
    """
    Testa se a Factory cria instâncias de ArxivDetailScraper corretamente.
    """
    scraper = ScraperFactory.create_scraper("2301.00001")
    assert isinstance(scraper, ArxivDetailScraper), (
        "A Factory deve criar uma instância de ArxivDetailScraper."
    )
    assert scraper.paper_id == "2301.00001", (
        "O ID do artigo deve ser configurado corretamente."
    )
