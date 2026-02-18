# HemnetHound

Stop guessing what sold for what. **HemnetHound** scrapes every sold listing you care about straight from [Hemnet](https://www.hemnet.se) and drops it into an interactive dashboard — so you can filter, compare, and download real Swedish property data in minutes, not hours.

---

## Overview

HemnetHound is a two-part tool built for anyone who wants a data-driven look at the Swedish real estate market:

1. **Crawler** — uses Selenium to load JavaScript-rendered Hemnet result pages and BeautifulSoup to extract structured listing data (price, size, area, monthly fee, and more).
2. **Dashboard** — a Streamlit app where you can kick off new scrape runs, explore the collected listings with live filters, and export everything as a CSV — no code required.

Whether you're tracking a neighbourhood, researching before a purchase, or just curious about the market, HemnetHound gives you the raw numbers without the manual copy-pasting.

---

## Short Demo

https://github.com/user-attachments/assets/84769665-9199-4013-a4eb-5be2811f5b81

---

## Features

- Crawl sold real estate listings from Hemnet using **Selenium + Chrome**
- Extract structured listing data: name, area, sold date, final price, price change %, size (m²), rooms, monthly fee, and price per m²
- Interactive **Streamlit** dashboard with two pages:
  - **📊 Data** — browse, filter, and download scraped listings as CSV
  - **🕷️ Scrape** — download fresh HTML pages and export to CSV, all from the UI
- Fast dependency management using **uv**

---

## Project Structure

```
app.py               # Streamlit entry point
main.py              # Standalone CLI crawler
pyproject.toml       # Project metadata & dependencies
crawlers/
  hemnet.py          # Scraping logic (BeautifulSoup)
  save_to_html.py    # Selenium page downloader
  export_to_csv.py   # CSV exporter
pages/
  1_📊_Data.py       # Data explorer page
  2_🕷️_Scrape.py     # Scrape control page
soups/               # Downloaded HTML pages (auto-created)
hemnet_data.csv      # Exported listings (auto-created)
```

---

## Requirements

- Python 3.14 or newer
- `uv` package manager
- Google Chrome (for Selenium)

---

## Installing uv

### macOS / Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```ps1
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Installation

Clone the repository:

```sh
git clone https://github.com/VAnkata19/Hemnet-Web-Crawler.git
cd Hemnet-Web-Crawler
```

Create a virtual environment and install dependencies:

```sh
uv venv .venv
uv sync
```

Activate the virtual environment:

### macOS / Linux

```sh
source .venv/bin/activate
```

### Windows (PowerShell)

```ps1
.venv\Scripts\activate
```

---

## Usage

### Streamlit Dashboard (recommended)

Launch the interactive app:

```sh
uv run streamlit run app.py
```

Then open http://localhost:8501 in your browser.

**Step 1 — Scrape page (🕷️)**  
Choose the number of Hemnet result pages to download (1–50) and click **Start downloading**. The raw HTML is saved to the `soups/` folder.

**Step 2 — Scrape page (🕷️)**  
Click **Export to CSV** to parse all downloaded HTML files and write the results to `hemnet_data.csv`.

**Data page (📊)**  
Browse the collected listings with sidebar filters (area, price range, free-text search), view summary metrics, and download the filtered data as CSV.

### CLI

Run the crawler from the terminal without the UI:

```sh
python main.py
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Dashboard UI |
| `selenium` | JavaScript-rendered page downloading |
| `beautifulsoup4` | HTML parsing |
| `pandas` | Data handling in the dashboard |

---

## Disclaimer

This project is intended for educational and personal use only.  
Please respect Hemnet’s terms of service and avoid excessive or aggressive crawling.
