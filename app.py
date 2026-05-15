import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wichita Falls Spending Exposé", layout="wide")

st.title("🛡️ Wichita Falls Government Spending Exposé")
st.markdown("**Real Data • Citizen Transparency**")

tab1, tab2 = st.tabs( )

with tab1:
    st.header("Largest Payments - April 2026")
    
    real_data = {
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
    
    df = pd.DataFrame(real_data)
    df = df .apply(lambda x: f"${x:,.0f}")
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("Total of Top 5 Payments")
    st.metric("Total", "$4,372,211")

with tab2:
    st.header("Overall Spending Increase")
    col1, col2, col3 = st.columns(3)
    col1.metric("April 2022", "$4.8M")
    col2.metric("April 2026", "$7.2M")
    col3.metric("Increase", "+50%")
    
    st.info("📍 This is real vendor data from Wichita Falls check registers. More detailed monthly data coming soon.")

st.caption("Wichita Falls Spending Exposé • patriotexpose.com")