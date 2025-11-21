from bs4 import BeautifulSoup




def categories_parser(results):
    for result in results:
        soup = BeautifulSoup(result, 'html.parser')
        title = soup.find('h1')
        articles = soup.find_all("article", class_="product_pod")
        books_links = [article.find("h3").find("a")["href"] for article in articles]
        print(f"Books for {title.string}: ")
        print(books_links)

