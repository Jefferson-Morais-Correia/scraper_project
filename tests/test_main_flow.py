from scraper_project.scrapers.arxiv_id_scraper import ArxivIdScraper
from scraper_project.scrapers.scraper_factory import ScraperFactory


def test_main_flow():
    """
    Testa o fluxo principal: obter IDs, criar scrapers e coletar dados.
    """
    id_scraper = ArxivIdScraper()
    ids = id_scraper.scrape(skip=0, show=10)
    assert len(ids) > 0, "O fluxo principal deve retornar ao menos um ID."

    results = []
    for paper_id in ids:
        scraper = ScraperFactory.create_scraper(paper_id)
        details = scraper.scrape()
        results.append(details)

    assert len(results) == len(ids), "Cada ID deve ter seus detalhes coletados."
