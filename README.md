# MarketBeacon: Competitive Intelligence Agent for B2B Companies

MarketBeacon is a lightweight, agent-based competitive intelligence system designed to autonomously monitor competitor activities and generate strategic insights. This tool is inspired by enterprise-grade solutions like Crayon and Klue, providing a cost-effective alternative for businesses to stay ahead in their market.

---

## Features

1. **Input Configuration**
   - Define your company and competitors in `config/companies.yaml`.

2. **Data Collection Agents**
   - **Web Scraper**: Scrapes competitor websites using Playwright and BeautifulSoup.
   - **News Agent**: Fetches news articles about competitors using SerpAPI.
   - **Pricing Agent**: Tracks pricing changes on competitor websites by scraping and comparing snapshots.
   - **Product Agent**: Scrapes changelogs and release notes to monitor product updates.
   - **Hiring Agent**: Scrapes LinkedIn to analyze hiring patterns of competitors.

3. **Data Storage**
   - **ChromaDB**: Stores embeddings of collected data for efficient retrieval.
   - **MongoDB**: Stores raw data collected by agents.

4. **Data Analysis**
   - **Gemini LLM**: Analyzes retrieved data and generates strategic insights.

5. **Orchestration**
   - A custom graph-based orchestrator wires all components together to ensure seamless execution of the workflow.

6. **Output**
   - Generates a weekly briefing report with strategic insights about competitors.

7. **Automation**
   - A scheduler automates the workflow to run at regular intervals (e.g., every Monday at 9:00 AM).

---

## Installation

### Prerequisites
- Python 3.10+
- MongoDB installed and running locally or on a remote server
- Git installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Pandey002/MarketBeacon.git
   cd MarketBeacon
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```

4. Set up your `.env` file with the following variables:
   ```env
   # MongoDB Configuration
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB=competitive_intel

   # API Keys
   GEMINI_API_KEY=your_gemini_api_key
   SERP_API_KEY=your_serp_api_key
   ```

5. Initialize the database:
   ```bash
   python db_init.py
   ```

---

## Usage

### Run the Project Manually
To run the entire workflow manually, execute the main script:
```bash
python main.py
```

### Automate with Scheduler
To run the workflow automatically at scheduled intervals, start the scheduler:
```bash
python scheduler.py
```
The scheduler is configured to run the workflow every Monday at 9:00 AM.

---

## Project Structure
```
MarketBeacon/
│
├── agents/
│   ├── hiring_agent.py         # Scrapes LinkedIn for hiring patterns
│   ├── news_agent.py           # Fetches news articles using SerpAPI
│   ├── pricing_agent.py        # Tracks pricing changes
│   ├── product_agent.py        # Scrapes changelogs and release notes
│   └── web_scraper.py          # General web scraping agent
│
├── analysis/
│   └── gemini_analyzer.py      # Analyzes data using Gemini LLM
│
├── config/
│   └── companies.yaml          # Configuration file for company and competitors
│
├── graph/
│   └── orchestrator.py         # Orchestrates the workflow using a custom graph
│
├── output/
│   └── briefing_builder.py     # Formats the final report
│
├── rag/
│   ├── embedder.py             # Stores embeddings in ChromaDB
│   └── retriever.py            # Retrieves data from ChromaDB
│
├── .env                        # Environment variables
├── db_init.py                  # Initializes the MongoDB database
├── requirements.txt            # Project dependencies
├── scheduler.py                # Automates the workflow
└── main.py                     # Entry point for the project
```

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---


