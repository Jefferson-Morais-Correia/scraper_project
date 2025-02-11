from abc import ABC, abstractmethod
from requests import Session


class BaseScraper(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.session = Session()

    @abstractmethod
    def scrape(self):
        pass
