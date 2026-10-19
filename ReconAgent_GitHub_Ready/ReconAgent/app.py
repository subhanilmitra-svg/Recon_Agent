import streamlit as st
import pandas as pd
from matcher import exact_match
from agent import resolve_exceptions

st.set_page_config(page_title="AI Finance Controller", layout="wide")
st.title("ReconAgent: AI-Powered Reconciliation")

st.write("Upload your synthetic data to start the reconciliation process.")

# Provide an option to load the pre-packaged sample data
use_sample = st.checkbox("Use sample synthetic data included in the project")

col1, col2 = st.columns(2)
with col1:
    bank_file = st.file_uploader("Upload Bank Statement (CSV)", type="csv")
with col2:
    rzp_file = st.file_uploader("Upload Razorpay Settlements (CSV)", type="csv")

if use_sample:
    bank_df = pd.read_csv("data/bank_statement.csv")
    rzp_df = pd.read_csv("data/razorpay_settlements.csv")
    st.success("Sample data loaded!")
elif bank_file and rzp_file:
    bank_df = pd.read_csv(bank_file)
    rzp_df = pd.read_csv(rzp_file)
    st.success("Custom data loaded!")
else:
    bank_df = pd.DataFrame()
    rzp_df = pd.DataFrame()

if not bank_df.empty and not rzp_df.empty:
    st.subheader("Data Preview")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Bank Data**")
        st.dataframe(bank_df)
    with c2:
        st.write("**Razorpay Data**")
        st.dataframe(rzp_df)
    
    if st.button("Run AI Reconciliation", type="primary"):
        with st.spinner("Running exact matches..."):
            matched, un_bank, un_rzp = exact_match(bank_df, rzp_df)
            
        st.success(f"Exact Matches Found: {len(matched)} / {max(len(bank_df), len(rzp_df))}")
        
        if not un_bank.empty and not un_rzp.empty:
            st.warning(f"Exceptions Found: {len(un_bank)} bank records and {len(un_rzp)} Razorpay records failed exact match.")
            
            with st.spinner("AI Agent resolving exceptions..."):
                ai_resolutions = resolve_exceptions(un_bank, un_rzp)
                
            st.subheader("AI Exception Resolutions")
            for res in ai_resolutions:
                st.json(res)
        else:
            st.success("100% Match Rate! No exceptions found.")
