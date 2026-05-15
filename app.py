import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending", layout="wide")
st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Tracking where your tax dollars are going**")

st.header("Spending Trends (2022 vs 2026)")

data = {
    "Category": ["Utilities", "Retirement & Benefits", "Water Infrastructure", "Contracted Services", "Communications"],
    "2022": [2500000, 450000, 500000, 300000, 200000],
    "2026": [3400000, 892000, 674000, 512000, 386000 "Increase" "2026" "2022" "2026" "2022" "2022"] * 100).round(1)

# Format the money columns
for col in :
    df = df .apply(lambda x: f"${x:,.0f}")

st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Overall Spending")
col1, col2, col3 = st.columns(3)
col1.metric("2022 Total", "$4.8M")
col2.metric("2026 Total", "$7.2M")
col3.metric("Increase", "+$2.4M", "50%")

st.info("📍 This is a demo using sample data. We'll load real check register data from the City of Wichita Falls soon.")