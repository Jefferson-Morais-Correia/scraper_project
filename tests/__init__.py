# Importa os testes de cada módulo de testes
from .test_arxiv_id_scraper import test_page_status_ok, test_get_ids
from .test_arxiv_detail_scraper import test_get_details
from .test_scraper_factory import test_factory_creates_scraper
from .test_main_flow import test_main_flow
from .test_utils import test_save_to_csv

# Lista de funções de teste disponíveis para exportação
__all__ = [
    "test_page_status_ok",
    "test_get_ids",
    "test_get_details",
    "test_factory_creates_scraper",
    "test_main_flow",
    "test_save_to_csv",
]
