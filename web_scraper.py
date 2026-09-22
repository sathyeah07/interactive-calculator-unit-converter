import requests
from bs4 import BeautifulSoup
import json


def scrape_quotes():
    url = "https://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = []

        for item in soup.select(".quote"):
            text = item.select_one(".text").get_text(strip=True)
            author = item.select_one(".author").get_text(strip=True)

            quotes.append({
                "quote": text,
                "author": author
            })

        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(quotes, file, indent=4, ensure_ascii=False)

        print("Scraping completed successfully!")
        print("Total quotes collected:", len(quotes))
        print("Saved to quotes.json")

    except requests.RequestException as error:
        print("Error while accessing website:", error)


if __name__ == "__main__":
    scrape_quotes()
