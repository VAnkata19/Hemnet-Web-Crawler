# 🏠 Hemnet Web Crawler

A Python-based web crawler for collecting property listing data from **Hemnet** (https://www.hemnet.se).

This project uses **`uv`** as a modern replacement for traditional Python tooling such as `pip` and `venv`.

---

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

## Installation
clone the repository:
```sh
git clone https://github.com/VAnkata19/Hemnet-Web-Crawler.git
cd Hemnet-Web-Crawler
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









