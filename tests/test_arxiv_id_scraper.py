import pytest
from scraper_project.scrapers.arxiv_id_scraper import ArxivIdScraper


@pytest.fixture
def id_scraper():
    return ArxivIdScraper()


def test_page_status_ok(id_scraper):
    """
    Testa se a página inicial retorna um status 200.
    """
    url = f"{id_scraper.BASE_URL}/list/cs.AI/recent?skip=0&show=20"
    response = id_scraper.session.get(url, verify=False)
    assert response.status_code == 200, (
        f"Status da página não é OK: {response.status_code}"
    )


def test_get_ids(id_scraper):
    """
    Testa se o método get_ids retorna uma lista com IDs.
    """
    ids = id_scraper.get_ids(skip=0, show=20)
    assert isinstance(ids, list), "O retorno deve ser uma lista."
    assert len(ids) > 0, "A lista deve conter IDs."
    assert all(isinstance(i, str) for i in ids), "Todos os IDs devem ser strings."
