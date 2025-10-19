"""
Day 06: Assignment_Text_Processor

Overview
--------
This day focuses on: Assignment_Text_Processor.
Practice inputs, sidebar config, dynamic display, downloads, and simple history.

Instructions
------------
- Read ./days/day_06/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st, io

st.set_page_config(page_title="Day 06 — Assignment", page_icon="📝")
st.title("📝 Day 06 — Breakout: Interactive Text Processor")
st.write("Open the assignment page at: `examples/assignment_text_processor/text_processor.py` in your repo.")

st.info("For convenience, a minimal inline demo is below. Use the full assignment file for the complete version.")

txt = st.text_area("Enter text")
opt = st.selectbox("Processing", ["Uppercase","Reverse"])
if st.button("Process"):
    out = txt.upper() if opt=="Uppercase" else txt[::-1]
    st.code(out)
    st.download_button("Download", out, file_name="processed.txt")
