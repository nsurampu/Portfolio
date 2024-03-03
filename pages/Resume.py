import streamlit as st
from streamlit_card import card


with st.sidebar:
    side_col1, side_col2 = st.columns([1, 2])
    side_col1.subheader('Get in touch!')
    side_col2.link_button("LinkedIn", "https://www.linkedin.com/in/naren-surampudi/")
    # st.image(image="https://github.com/nsurampu/Portfolio/blob/main/images/gatech.png?raw=true")

tab1, tab2 = st.tabs(["Resume", "CV"])

with tab1:
    st.download_button("Download Resume", data="")
    st.markdown("*Resume yet to be added*")

with tab2:
    st.download_button("Download CV", data="")
    st.markdown("*CV yet to be added*")