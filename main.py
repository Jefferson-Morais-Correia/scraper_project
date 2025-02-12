from scrapers.arxiv_id_scraper import ArxivIdScraper
from scrapers.scraper_factory import ScraperFactory
from utils.helpers import save_to_csv
import pandas as pd
from utils.logging_config import setup_logger


logger = setup_logger("arxiv_scraper")


def main():
    logger.info("Iniciando o scraping do arXiv...")

    # Passo 1: Obter os IDs dos artigos
    id_scraper = ArxivIdScraper()
    ids = id_scraper.scrape(skip=0, show=200)  # Pegue os IDs da página inicial
    logger.info(f"{len(ids)} IDs encontrados.")

    # Passo 2: Obter os detalhes de cada artigo
    titles, abstracts, references = [], [], []
    for paper_id in ids[:10]:  # Limite para 10 artigos como exemplo
        logger.info(f"Processando artigo com ID: {paper_id}")
        scraper = ScraperFactory.create_scraper(paper_id)
        try:
            details = scraper.scrape()
            titles.append(details["Title"])
            abstracts.append(details["Abstract"])
            references.append(details["References"])
        except Exception as e:
            logger.error(f"Erro ao processar o artigo {paper_id}: {e}")

    # Passo 3: Salvar os resultados em um arquivo CSV
    data = pd.DataFrame(
        {"Title": titles, "Abstract": abstracts, "References": references}
    )
    save_to_csv(data, "arxiv_papers.csv")
    logger.info("Scraping finalizado. Dados salvos em 'arxiv_papers.csv'.")


if __name__ == "__main__":
    main()
