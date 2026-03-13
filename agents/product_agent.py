# Product Agent
# This agent scrapes changelogs and release notes from competitor websites.

from agents.web_scraper import scrape_website


def extract_changelog_data(soup):
    # Implement logic to extract changelog/release note data from the BeautifulSoup object
    changelog_data = []
    for entry in soup.select(".changelog-entry"):
        title = entry.select_one(".entry-title").text.strip()
        date = entry.select_one(".entry-date").text.strip()
        description = entry.select_one(".entry-description").text.strip()
        changelog_data.append({
            "title": title,
            "date": date,
            "description": description
        })
    return changelog_data

if __name__ == "__main__":
    url = "https://example.com/changelog"  # Replace with the target URL
    soup = scrape_website(url)
    changelog_data = extract_changelog_data(soup)

    if changelog_data:
        print("Changelog/Release Notes:")
        for entry in changelog_data:
            print(f"- {entry['date']}: {entry['title']}\n  {entry['description']}")
    else:
        print("No changelog or release notes found.")
        print("No changelog or release notes found.")
