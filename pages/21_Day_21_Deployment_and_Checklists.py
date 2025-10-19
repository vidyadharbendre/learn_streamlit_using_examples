"""
Day 21: Deployment_and_Checklists

Overview
--------
This day focuses on: Deployment_and_Checklists.
Package, pin dependencies, and deploy to a host.

Instructions
------------
- Read ./days/day_21/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st

st.set_page_config(page_title="Day 21 — Deployment & Checklists", page_icon="🚢", layout="centered")
st.title("🚢 Day 21 — Deployment & Checklists")

st.subheader("Targets")
st.write("- Streamlit Community Cloud")
st.write("- Render / Railway (optional)")

with st.expander("Deployment Checklist"):
    st.markdown(
        "- requirements.txt pinned\n"
        "- App entry selected (Home.py)\n"
        "- Secrets (if any) managed via UI, never hard-coded\n"
        "- Test on fresh environment before pushing"
    )

st.success("You’re ready to deploy!")
