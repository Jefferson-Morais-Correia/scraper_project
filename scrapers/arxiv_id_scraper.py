from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class ArxivIdScraper(BaseScraper):
    BASE_URL = "https://arxiv.org"

    def get_ids(self, skip=0, show=2000):
        url = f"{self.BASE_URL}/list/cs.AI/recent?skip={skip}&show={show}"
        response = self.session.get(url, verify=False)
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch data, status code: {response.status_code}"
            )

        soup = BeautifulSoup(response.content, "html.parser")
        tags = soup.find_all(
            lambda tag: tag.has_attr("title") and tag["title"] == "Abstract"
        )
        ids = [tag.text.strip().split(":")[1] for tag in tags]

        return ids
