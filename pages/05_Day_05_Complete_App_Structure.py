"""
Day 05: Complete_App_Structure

Overview
--------
This day focuses on: Complete_App_Structure.
Tie together state, chat UI, sidebar, and metrics in one flow.

Instructions
------------
- Read ./days/day_05/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st, time, random
from datetime import datetime

st.set_page_config(page_title="Day 05 — Complete App Structure", page_icon="🚀", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"Hello! How can I help?","timestamp": datetime.now()}]
if "stats" not in st.session_state:
    st.session_state.stats = {"total": 0, "start": datetime.now()}

st.title("🚀 Day 05 — Complete App Structure")

# Sidebar
with st.sidebar:
    st.header("Settings")
    style = st.selectbox("Style", ["Friendly","Professional","Creative"], 0)

# History
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.caption(m.get("timestamp", datetime.now()).strftime("%H:%M:%S"))
        st.write(m["content"])

# Input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role":"user","content": prompt, "timestamp": datetime.now()})
    st.session_state.stats["total"] += 1
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(random.uniform(0.4,1.2))
        reply = f"[{style}] Thanks for: '{prompt}'"
        st.write(reply)
    st.session_state.messages.append({"role":"assistant","content": reply, "timestamp": datetime.now()})
    st.rerun()

st.metric("Total Messages", st.session_state.stats["total"])

with st.expander("🎓 Teaching Notes"):
    st.markdown("- Page config → init → sidebar → main → notes\n- Gentle guards and trimmed history are production basics")
