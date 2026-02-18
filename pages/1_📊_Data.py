import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Hemnet Data", page_icon="📊", layout="wide")

st.title("📊 Hemnet — Sold Listings")

CSV_FILE = "hemnet_data.csv"

if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
    st.warning("No data found. Go to the **Scrape** page to collect data first.")
    st.stop()

df = pd.read_csv(CSV_FILE)

# ── Sidebar filters ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")

    search = st.text_input("🔍 Search (name / area)", "")

    areas = sorted(df["Area"].dropna().unique().tolist())
    selected_areas = st.multiselect("Area", areas)

    price_min, price_max = int(df["Final price (kr)"].str.replace(r"[^\d]", "", regex=True).astype(int).min()), \
                           int(df["Final price (kr)"].str.replace(r"[^\d]", "", regex=True).astype(int).max())
    price_range = st.slider("Final price (kr)", price_min, price_max, (price_min, price_max), step=50_000)

# ── Apply filters ─────────────────────────────────────────────────────────────
filtered = df.copy()

# Parse price as int for filtering
filtered["_price_int"] = filtered["Final price (kr)"].str.replace(r"[^\d]", "", regex=True).astype(int)

if search:
    mask = filtered["Name"].str.contains(search, case=False, na=False) | \
           filtered["Area"].str.contains(search, case=False, na=False)
    filtered = filtered[mask]

if selected_areas:
    filtered = filtered[filtered["Area"].isin(selected_areas)]

filtered = filtered[(filtered["_price_int"] >= price_range[0]) & (filtered["_price_int"] <= price_range[1])]
filtered = filtered.drop(columns=["_price_int"])

# ── Metrics ───────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
prices = filtered["Final price (kr)"].str.replace(r"[^\d]", "", regex=True).astype(int)

col1.metric("Listings shown", len(filtered))
col2.metric("Avg. price", f"{prices.mean():,.0f} kr" if len(filtered) else "—")
col3.metric("Median price", f"{prices.median():,.0f} kr" if len(filtered) else "—")

st.divider()

# ── Table ─────────────────────────────────────────────────────────────────────
st.dataframe(
    filtered.reset_index(drop=True),
    use_container_width=True,
    height=600,
)

# ── Download ──────────────────────────────────────────────────────────────────
st.download_button(
    label="⬇ Download filtered CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="hemnet_filtered.csv",
    mime="text/csv",
)
