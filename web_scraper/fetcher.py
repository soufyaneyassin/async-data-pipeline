import requests
from typing import List
from bs4 import BeautifulSoup
#in this file we will scrap the "books to scrape" website


def get_categories(url: str) -> List[str]:
        try:
            response = requests.get(url)
        except Exception as e:
               print(f"Something went wrong while getting data from {url}, ERROR: {e}")

        # Trying BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        categories = soup.find('div', class_="side_categories").find_all('a')

        #extract categories links
        links = []
        for category in categories:
            links.append(category.get('href'))
        return links







