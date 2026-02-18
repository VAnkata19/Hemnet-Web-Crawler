import streamlit as st
import sys
import os

# Ensure project root is on the path so crawlers package is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import crawlers

st.set_page_config(page_title="Scrape Hemnet", page_icon="🕷️", layout="centered")

st.title("🕷️ Scrape Hemnet")
st.markdown(
    """
    This page controls the crawler.  
    **Step 1** downloads raw HTML pages from Hemnet into the `soups/` folder.  
    **Step 2** parses those pages and exports the results to `hemnet_data.csv`.
    """
)

st.divider()

# ── Step 1: Download HTML pages ───────────────────────────────────────────────
st.subheader("Step 1 — Download pages")
st.info(
    "Uses **Selenium + Chrome** to load each Hemnet results page and saves the "
    "HTML to `soups/`. This can take a while depending on how many pages are set.",
    icon="ℹ️",
)

num_pages = st.number_input("Number of pages to download", min_value=1, max_value=50, value=4)

if st.button("▶ Start downloading", type="primary"):
    urls = crawlers.get_urls()[:num_pages]
    progress = st.progress(0, text="Starting…")
    log = st.empty()

    os.makedirs("soups", exist_ok=True)

    for i, url in enumerate(urls, start=1):
        log.info(f"Downloading page {i}/{len(urls)}: {url}")
        try:
            crawlers.save_to_html([url])
        except Exception as e:
            st.error(f"Failed on page {i}: {e}")
            break
        progress.progress(i / len(urls), text=f"Page {i}/{len(urls)} done")

    progress.progress(1.0, text="Download complete ✅")
    st.success(f"Saved {num_pages} page(s) to `soups/`.")

st.divider()

# ── Step 2: Parse & export ────────────────────────────────────────────────────
st.subheader("Step 2 — Parse & export to CSV")

soup_files = [f for f in os.listdir("soups") if f.endswith(".html")] if os.path.isdir("soups") else []
st.write(f"Found **{len(soup_files)}** HTML file(s) in `soups/`:")
if soup_files:
    st.code("\n".join(sorted(soup_files)))

if st.button("▶ Scrape & export", type="primary", disabled=len(soup_files) == 0):
    with st.spinner("Scraping…"):
        try:
            data = crawlers.scrape()
            crawlers.export(
                filename="hemnet_data.csv",
                name=data[0],
                area=data[1],
                sold_date=data[2],
                price=data[3],
                procent=data[4],
                square_meter=data[5],
                rooms=data[6],
                monthly_fee=data[7],
                price_per_square_meter=data[8],
            )
            st.success(f"✅ Exported **{len(data[0])}** listings to `hemnet_data.csv`.")
            st.balloons()
        except Exception as e:
            st.error(f"Scraping failed: {e}")
