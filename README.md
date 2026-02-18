# HemnetHound

A Python-based web crawler for collecting property listing data from **Hemnet** (https://www.hemnet.se).

---

## Short Demo

https://github.com/user-attachments/assets/84769665-9199-4013-a4eb-5be2811f5b81

## Features

- Crawl real estate listings from Hemnet
- Extract structured listing data
- Simple and extensible Python architecture
- Fast dependency management using **uv**

---

## Requirements

- Python 3.10 or newer
- `uv` package manager

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
clone the repository:
```sh
git clone https://github.com/VAnkata19/Hemnet-Web-Crawler.git
cd HemnetHound
```

Create a virtual environment using `uv`:
```sh
uv venv .venv
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

Install project dependencies:
```sh
uv sync
```

--- 

## Usage

Run the crawler with:
```sh
python main.py
```
The script will:
   Start crawling Hemnet listing pages
   Extract relevant property data
   Save the collected data locally for further analysis
You can customize crawl targets, filters, and scraping logic directly in the source code.


## Disclaimer
This project is intended for educational and personal use only.
Please respect Hemnet’s terms of service and avoid excessive or aggressive crawling.



