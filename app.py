import streamlit as st
import pandas as pd
import plotly.express as px

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
    
    # Bar chart
    fig_bar = px.bar(
        df,
        x="Category",
        y="Increase",
        text="Increase",
        title="Spending Increase by Category (2022 → 2026)",
        color="Category"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Pie chart
    fig_pie = px.pie(
        df,
        names="Category",
        values="April 2026",
        title="2026 Spending Breakdown"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.caption("Wichita Falls Spending Exposé • Live Dashboard")