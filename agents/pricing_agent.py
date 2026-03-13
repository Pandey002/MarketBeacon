# Pricing Agent
# This agent uses the web scraper internally and adds diff/snapshot logic to track pricing changes.

import json
import os
from datetime import datetime

from agents.web_scraper import scrape_website


def extract_pricing_data(soup):
    # Implement logic to extract pricing data from the BeautifulSoup object
    # Example: Find elements with specific classes or IDs
    pricing_data = {}
    for product in soup.select(".product-item"):
        name = product.select_one(".product-name").text.strip()
        price = product.select_one(".product-price").text.strip()
        pricing_data[name] = price
    return pricing_data

def save_snapshot(data, filename="pricing_snapshot.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_snapshot(filename="pricing_snapshot.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def compare_snapshots(old_snapshot, new_snapshot):
    changes = {}
    for product, new_price in new_snapshot.items():
        old_price = old_snapshot.get(product)
        if old_price != new_price:
            changes[product] = {"old": old_price, "new": new_price}
    return changes

if __name__ == "__main__":
    url = "https://example.com/pricing"  # Replace with the target URL
    soup = scrape_website(url)
    new_snapshot = extract_pricing_data(soup)

    old_snapshot = load_snapshot()
    changes = compare_snapshots(old_snapshot, new_snapshot)

    if changes:
        print("Pricing changes detected:")
        print(json.dumps(changes, indent=4))
    else:
        print("No pricing changes detected.")

    save_snapshot(new_snapshot)

    save_snapshot(new_snapshot)
