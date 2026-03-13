# News Agent
# This agent uses SerpAPI to fetch news articles related to competitors.

import os

import requests


def fetch_news(query):
    api_key = os.getenv("SERP_API_KEY")
    if not api_key:
        raise ValueError("SERP_API_KEY is not set in the environment variables.")

    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "tbm": "nws",
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch news: {response.status_code}, {response.text}")

if __name__ == "__main__":
    query = "competitor news"  # Replace with your query
    news_data = fetch_news(query)
    print(news_data)
    news_data = fetch_news(query)
    print(news_data)
