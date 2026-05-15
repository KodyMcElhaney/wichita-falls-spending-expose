import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending Exposé", layout="wide")

st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Citizen-led transparency • Tracking where your tax dollars go**")

tab1, tab2 = st.tabs(["📊 Data Table", "📈 Charts"])

with tab1:
    st.header("Spending Trends: April 2022 vs April 2026")
    
    # Sample data (we'll load real check-register data later)
    data = {
        "Category": ["Utilities", "Retirement & Benefits", "Water Infrastructure", "Contracted Services", "Communications"],
        "April 2022": [2_500_000, 450_000, 500_000, 300_000, 200_000],
        "April 2026": [3_400_000, 892_000, 674_000, 512_000, 386_000]
    }
    
    df = pd.DataFrame(data)
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
            "% Change": st.column_config.NumberColumn("% Change", format="%.1f%%")
        }
    )
    
    st.subheader("Overall Change")
    col1, col2, col3 = st.columns(3)
    col1.metric("April 2022 Total", "$4.80M")
    col2.metric("April 2026 Total", "$7.20M")
    col3.metric("Increase", "+$2.40M", "50%")

with tab2:
    st.header("Visual Charts")
    
    # Bar chart (built-in)
    st.subheader("Spending Increase by Category")
    chart_data = df.set_index("Category")["Increase"]
    st.bar_chart(chart_data, use_container_width=True)
    
    # Pie chart (built-in)
    st.subheader("2026 Spending Breakdown")
    pie_data = df.set_index("Category")["April 2026"]
    st.pyplot(pie_data.plot.pie(autopct='%1.1f%%', figsize=(8, 8)).figure)

st.caption("Wichita Falls Spending Exposé • Live Dashboard")