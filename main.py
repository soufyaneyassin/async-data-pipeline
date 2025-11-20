from dotenv import load_dotenv
import os
from web_scraper.fetcher import get_categories
from web_scraper.async_fetcher import walk_through_links
import asyncio


def main():
    load_dotenv()
    url = os.getenv("WEBSITE_URL")
    links = get_categories(url)
    results = asyncio.run(walk_through_links(links))
    #TO DO: after fetching each category, we should use beautiful soup to process each category, structure books data...