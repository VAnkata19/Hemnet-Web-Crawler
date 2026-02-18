import streamlit as st

st.set_page_config(page_title="Hemnet Crawler", page_icon="🏠", layout="centered")

st.title("🏠 Hemnet Web Crawler")
st.markdown(
    """
    Welcome! Use the sidebar to navigate between pages.

    | Page | Description |
    |------|-------------|
    | 📊 **Data** | Browse, filter and download the scraped listings |
    | 🕷️ **Scrape** | Download fresh HTML pages and export to CSV |
    """
)
