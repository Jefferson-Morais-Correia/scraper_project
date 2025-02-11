from .arxiv_detail_scraper import ArxivDetailScraper


class ScraperFactory:
    @staticmethod
    def create_scraper(paper_id):
        return ArxivDetailScraper(paper_id)
