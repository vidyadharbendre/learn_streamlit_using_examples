
"""
Streamlit 21‑Day Mini‑Bootcamp — Home

How to use
----------
- Use the left sidebar to navigate pages (Day 01 to Day 21).
- Each day has: a runnable demo, exercises, and a README under ./days/day_XX/README.md
- Re-run any page from the "R" button in the Streamlit toolbar.

> Note: This 21-day plan wraps your earlier examples:
> - Day 1 wraps `examples/01_hello_world_reruns/app.py` (rerun model)
> - Day 2 wraps `examples/02_session_state_basics/app.py` (session state)
> - Day 3 wraps `examples/03_chat_interface_basics/app.py` (chat UI)
> - Day 4 wraps `examples/04_sidebar_controls_config/app.py` (sidebar/config)
> - Day 5 wraps `examples/05_complete_app/app.py` (complete app structure)
> - Day 6 includes the Assignment `examples/assignment_text_processor/text_processor.py`

"""
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Streamlit 21‑Day Mini‑Bootcamp", page_icon="🎓", layout="wide")

st.title("🎓 Streamlit 21‑Day Mini‑Bootcamp")
st.write("Build production‑ready Streamlit skills step by step — one focused topic per day.")

st.markdown("""
### What you'll practice
- Rerun mental model • Session state • Chat UI • Sidebar & config • Complete app patterns
- Forms & callbacks • Caching • File uploads • DataFrames & basic charts
- Multi‑page navigation • Theming • Error handling • Simple auth gate patterns
- External API calls (mock) • Logging & config • Testing helpers • Deployment checklists
""")

st.info("Use the **Pages** menu (left sidebar) to jump to any day.")

st.caption(f"Generated on: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")
