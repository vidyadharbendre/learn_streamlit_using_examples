"""
Day 01: Rerun_Model

Overview
--------
This day focuses on: Rerun_Model.
You’ll observe counters resetting without session_state and stabilizing with it.

Instructions
------------
- Read ./days/day_01/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st

st.set_page_config(page_title="Day 01 — Rerun Model", page_icon="🌀")
st.title("🌀 Day 01 — Rerun Model")

st.write("Streamlit reruns your script top→bottom on each interaction.")

if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.metric("Rerun Counter", st.session_state.counter)

val = st.slider("Move me to trigger reruns", 0, 100, 50)
st.write(f"Slider value: {val}")

with st.expander("🎓 Teaching Notes"):
    st.markdown(
        "- **Reruns:** Every widget interaction reruns the whole script.\n"
        "- **State:** Use `st.session_state` to persist values across reruns."
    )
