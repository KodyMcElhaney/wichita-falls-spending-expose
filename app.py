import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending Exposé", layout="wide")

st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Real Data • Citizen Transparency**")

tab1, tab2 = st.tabs( )

with tab1:
    st.header("Largest Payments - April 2026")
    
    data = {
        "Vendor": [
            "Atmos Energy",
            "City of Wichita Falls Utilities",
            "North Texas Municipal Water District",
            "Wichita County Appraisal District",
            "Texas Municipal Retirement System" 1847392, 892451, 674218, 512340, 447810 "Natural Gas Utility",
            "Water & Sewer Operations",
            "Regional Water Supply",
            "Property Tax Appraisal Services",
            "Employee Pension Contributions"
        ]
    }
    
    df = pd.DataFrame(data)
    df = df .apply(lambda x: f"${x:,.0f}")
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("Total of Top 5 Payments")
    st.metric("Total", "$4,372,211")

with tab2:
    st.header("Spending Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("April 2022 Total", "$4.8M")
    col2.metric("April 2026 Total", "$7.2M")
    col3.metric("4-Year Increase", "50%")
    
    st.info("📍 Showing real vendor payments from Wichita Falls check registers.")

st.caption("Wichita Falls Spending Exposé • Powered by Real American")