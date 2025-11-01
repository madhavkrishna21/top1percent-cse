# day3.py - Top 1% Web App (Streamlit)
import streamlit as st

st.set_page_config(page_title="Madhav's 1% Dashboard", layout="centered")

st.title("🚀 Madhav Krishna")
st.subheader("Grade 12 → AI Startup 2030")

st.write("""
**Day 0**: Goal locked  
**Day 1**: Tip Calculator (OOP)  
**Day 2**: To-Do CLI (JSON)  
**Day 3**: This web app — LIVE  
""")

name = st.text_input("Your Name")
goal = st.text_input("Your 2030 Goal")

if st.button("Lock In"):
    st.success(f"{name}, your goal '{goal}' is locked!")
    st.balloons()

st.markdown("---")
st.caption("Built with Streamlit | No IIT. Just proof.")
