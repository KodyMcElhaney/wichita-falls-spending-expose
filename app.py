import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending", layout="wide")
st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Tracking where your tax dollars are going**")

st.header("Spending Trends (2022 - 2026)")

data = {
    "Category": ["Utilities", "Retirement", "Water", "Contracted Services", "Communications"],
    "2022": [2500000, 450000, 500000, 300000, 200000],
    "2026": [3400000, 892000, 674000, 512000, 386000 "2026" "2022" "2026" "2022"]) / df["2022"] * 100).round(1)

st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Total Spending Increase")
st.metric("From 2022 to 2026", "$4.8M → $7.2M", "+50%")

st.info("📍 This is a demo dashboard. Real check register data will be added soon.")
