# Web Scraper Agent
# This agent uses Playwright and BeautifulSoup to scrape competitor websites.

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def scrape_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, 'html.parser')
    return soup

if __name__ == "__main__":
    url = "https://example.com"  # Replace with the target URL
    data = scrape_website(url)
    print(data.prettify())
    print(data.prettify())
