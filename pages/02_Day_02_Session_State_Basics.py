"""
Day 02: Session_State_Basics

Overview
--------
This day focuses on: Session_State_Basics.
Initialize, mutate, and read keys; show simple history.

Instructions
------------
- Read ./days/day_02/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st

st.set_page_config(page_title="Day 02 — Session State Basics", page_icon="🧠")
st.title("🧠 Day 02 — Session State Basics")

if "count" not in st.session_state:
    st.session_state.count = 0
if "history" not in st.session_state:
    st.session_state.history = []

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Increment"):
        st.session_state.count += 1
        st.session_state.history.append(("inc", st.session_state.count))
with col2:
    if st.button("➖ Decrement"):
        st.session_state.count -= 1
        st.session_state.history.append(("dec", st.session_state.count))
with col3:
    if st.button("🔄 Reset"):
        st.session_state.count = 0
        st.session_state.history.clear()

st.metric("Current Count", st.session_state.count)
with st.expander("History"):
    st.write(st.session_state.history)

with st.expander("🎓 Teaching Notes"):
    st.markdown("- Initialize keys before use\n- Avoid KeyErrors by checking membership")
