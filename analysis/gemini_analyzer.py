# Gemini Analyzer
# This module uses the Gemini LLM to analyze retrieved data and generate insights.

import os

import requests


def analyze_with_gemini(prompt):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

    url = "https://api.gemini.com/v1/analyze"
    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": prompt}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to analyze with Gemini: {response.status_code}, {response.text}")

if __name__ == "__main__":
    prompt = "Summarize the latest competitor updates."
    analysis = analyze_with_gemini(prompt)
    print("Analysis Results:")
    print(analysis)
    print("Analysis Results:")
    print(analysis)
