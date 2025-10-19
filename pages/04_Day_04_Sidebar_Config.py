"""
Day 04: Sidebar_Config

Overview
--------
This day focuses on: Sidebar_Config.
Keep controls in the sidebar; reflect impact in main panel with metrics/notes.

Instructions
------------
- Read ./days/day_04/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st

st.set_page_config(page_title="Day 04 — Sidebar & Config", page_icon="⚙️", layout="wide")
st.title("⚙️ Day 04 — Sidebar Controls & Configuration")

if "settings" not in st.session_state:
    st.session_state.settings = {"model": "GPT-3.5", "temperature": 0.7, "max_tokens": 150}

with st.sidebar:
    st.header("Config")
    model = st.selectbox("Model", ["GPT-3.5", "GPT-4", "Claude", "Llama 2"], index=0)
    temp = st.select_slider("Temperature", options=[0.0,0.5,1.0,1.5,2.0], value=0.7)
    max_tokens = st.number_input("Max Tokens", 50, 2000, 150, 50)

    if st.button("Save"):
        st.session_state.settings = {"model": model, "temperature": float(temp), "max_tokens": int(max_tokens)}
        st.toast("Saved.", icon="✅")

col1, col2 = st.columns([2,1])
with col1:
    st.subheader("Current Settings")
    st.table({"Setting": list(st.session_state.settings.keys()), "Value": list(st.session_state.settings.values())})
with col2:
    st.subheader("Impact")
    t = st.session_state.settings["temperature"]
    if t < 0.5: st.info("Focused")
    elif t < 1.0: st.info("Balanced")
    else: st.warning("Creative")

with st.expander("🎓 Teaching Notes"):
    st.markdown("- Sidebar for knobs; main area for effects\n- Persist normalized settings back into state")
