"""
Day 03: Chat_Interface_Basics

Overview
--------
This day focuses on: Chat_Interface_Basics.
Use `st.chat_message` + `st.chat_input`; maintain a simple message schema.

Instructions
------------
- Read ./days/day_03/README.md
- Run this page and try the mini‑lab exercises.
- Use the expander at the bottom for Teaching Notes.
"""

import streamlit as st, random, time

st.set_page_config(page_title="Day 03 — Chat Interface", page_icon="💬")
st.title("💬 Day 03 — Chat Interface Basics")

if "chat" not in st.session_state:
    st.session_state.chat = [{"role": "assistant", "content": "Hello! Try sending me a message."}]

for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Type your message"):
    st.session_state.chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            time.sleep(0.6)
        reply = random.choice([
            f"I read: '{prompt}'",
            f"You said '{prompt}'. Nice!",
        ])
        st.write(reply)
    st.session_state.chat.append({"role": "assistant", "content": reply})

with st.expander("🎓 Teaching Notes"):
    st.markdown("- Maintain messages as a list of dicts `{role, content}`\n- Render old messages before new input")
