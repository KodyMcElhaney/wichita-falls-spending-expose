import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending Exposé", layout="wide")

st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Citizen-led transparency • Tracking where your tax dollars go**")

st.header("Spending Trends: April 2022 vs April 2026")

# Sample data (we'll replace with real data later)
data = {
    "Category": [
        "Utilities", 
        "Retirement & Benefits", 
        "Water Infrastructure", 
        "Contracted Services", 
        "Communications"
    ],
    "April 2022": [2500000, 450000, 500000, 300000, 200000],
    "April 2026": [3400000, 892000, 674000, 512000, 386000]
}

df = pd.DataFrame(data)

# Calculate increase
df["Increase"] = df["April 2026"] - df["April 2022"]
df["% Change"] = ((df["April 2026"] - df["April 2022"]) / df["April 2022"] * 100).round(1)

# Format money columns nicely
for col in ["April 2022", "April 2026", "Increase"]:
    df[col] = df[col].apply(lambda x: f"${x:,.0f}")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Category": st.column_config.TextColumn("Category"),
        "% Change": st.column_config.NumberColumn("% Change", format="%.1f%%")
    }
)

st.subheader("Overall Change")
col1, col2, col3 = st.columns(3)
col1.metric("April 2022 Total", "$4.80M")
col2.metric("April 2026 Total", "$7.20M", "↑ $2.40M")
col3.metric("4-Year Increase", "50%")

st.info("📍 This dashboard uses sample data for demonstration. Real monthly check register data will be loaded soon.")

st.caption("Wichita Falls Spending Exposé • Built for transparency")