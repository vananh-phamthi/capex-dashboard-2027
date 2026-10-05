from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CAPEX Dashboard 2027 & Business Plan 2027-2031",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Optimize full screen layout while preserving Streamlit manage status if needed
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        .block-container {padding: 0.2rem 0.5rem 0 0.5rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_html():
    p = Path(__file__).parent / "dashboard.html"
    return p.read_text(encoding="utf-8")

try:
    html_content = load_html()
    components.html(html_content, height=2600, scrolling=True)
except Exception as e:
    st.error(f"Error loading dashboard: {e}")
