from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="DIGITAL | Image Processing Lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

# Render the existing self-contained HTML interface inside Streamlit.
components.html(html, height=1100, scrolling=True)
