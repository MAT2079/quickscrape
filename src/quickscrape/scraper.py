import requests
from bs4 import BeautifulSoup


def scrape_to_markdown(url: str, out_path: str) -> None:
    """Download a URL and save its plain text into a Markdown file."""
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n")

    if not out_path.lower().endswith(".md"):
        out_path += ".md"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
