from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class ArxivDetailScraper(BaseScraper):
    BASE_URL = "https://arxiv.org"

    def __init__(self, paper_id):
        super().__init__()
        self.paper_id = paper_id

    def get_details(self):
        paper_url = f"{self.BASE_URL}/html/{self.paper_id}"
        response = self.session.get(paper_url, verify=False)
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch details for paper ID {self.paper_id}, status code: {response.status_code}"
            )

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find(class_="ltx_title").text.strip()
        abstract = soup.find(class_="ltx_abstract").text.strip()
        bibliography = soup.find(class_="ltx_bibliography").text.strip()

        return {"Title": title, "Abstract": abstract, "References": bibliography}
