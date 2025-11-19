from dotenv import load_dotenv
import os
from web_scraper.fetcher import get_categories


def main():
    load_dotenv()
    url = os.getenv("WEBSITE_URL")
    links = get_categories(url)
    #TO DO: async fetching of each link, using a dedicated async_fetcher module