import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Wichita Falls Spending Exposé", layout="wide")

st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Tracking where your tax dollars are going**")

tab1, tab2 = st.tabs( )

with tab1:
    st.header("Spending Trends: 2022 vs 2026")
    
    data = {
        "Category": ["Utilities", "Retirement", "Water", "Contracted Services", "Communications"],
        "2022": [2500000, 450000, 500000, 300000, 200000],
        "2026": [3400000, 892000, 674000, 512000, 386000 "2026" "2022" "2026" "2022"]) / df["2022" "2022", "2026", "Increase"]:
        df = df .apply(lambda x: f"${x:,.0f}")
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("2022 Total", "$4.8M")
    col2.metric("2026 Total", "$7.2M")
    col3.metric("Increase", "+50%")

with tab2:
    st.header("Visual Charts")
    fig = px.bar(df, x="Category", y="Increase", title="Spending Increase by Category", text="Increase")
    st.plotly_chart(fig, use_container_width=True)
    
    fig2 = px.pie(df, names="Category", values="2026", title="2026 Spending Breakdown")
    st.plotly_chart(fig2, use_container_width=True)

st.caption("Wichita Falls Spending Exposé • Live Dashboard")