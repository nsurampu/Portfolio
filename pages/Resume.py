import streamlit as st
from streamlit_card import card


with st.sidebar:
    card(title="LinkedIn", text="LinkedIn", url="https://www.linkedin.com/in/naren-surampudi/")

tab1, tab2 = st.tabs(["Resume", "CV"])

with tab1:
    st.download_button("Download Resume", data="")
    st.markdown("Put resume here")

with tab2:
    st.download_button("Download CV", data="")
    st.markdown("Put CV here")