import requests
from bs4 import BeautifulSoup

def search_flipkart(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    url = f"https://www.flipkart.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    product_cards = soup.select("div._1AtVbE")  # Outer container
    for card in product_cards:
        name_tag = card.select_one("div._4rR01T") or card.select_one("a.IRpwTa")
        price_tag = card.select_one("div._30jeq3")
        link_tag = card.find("a", href=True)

        if name_tag and price_tag and link_tag:
            product = {
                "title": name_tag.get_text(strip=True),
                "price": price_tag.get_text(strip=True),
                "link": "https://www.flipkart.com" + link_tag['href']
            }
            results.append(product)

    return results

