
import re
import sys
import requests


def get_page_title(url: str) -> str:
    """Fetch a webpage and return the text inside its <title> tag."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; TitleScraper/1.0)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # raise an error for bad status codes (404, 500, etc.)

    match = re.search(r"<title.*?>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    if match:
        # Collapse whitespace/newlines that sometimes appear inside <title>
        return " ".join(match.group(1).split())
    return "Title not found"


def scrape_and_save(url: str, output_file: str) -> None:
    try:
        title = get_page_title(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\n")
        f.write(f"Title: {title}\n")

    print(f"Page title: {title}")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        page_url, out_file = sys.argv[1], sys.argv[2]
    else:
        page_url = input("Enter the webpage URL: ").strip()
        out_file = input("Enter path for output .txt file: ").strip()

    scrape_and_save(page_url, out_file)
