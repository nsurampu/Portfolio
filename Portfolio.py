import streamlit as st
from streamlit_timeline import timeline
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
from streamlit_pdf_viewer import pdf_viewer
import base64

st.set_page_config(page_title='Welcome!', layout='wide')


tab1, tab2 = st.tabs(["Portfolio", "Resume"])

with tab1:

    st.header("Hi, I'm Naren Surampudi!")

    intro_body = '''
    And I like to refer to myself as an accidental data professional. Why is that? Well, I wasn't a big fan of numbers and math during my schooling days. If you had told my school-boy self that one day he would be working with math and numbers day-in and day-out,
    I'd bet he'd be quite shocked (and maybe a little bit crestfallen).\n
    Then how did I land up in this space? Well, I first fell in love with all things **Data**, **AI** and **Machine Learning** during college, when I came across a simple tutorial for predicting house prices. Looking back, it was
    a really simple thing, but at that time, it blew my mind. That took me down the data rabbit hole that I doubt I'll try to get out of anytime soon.\n
    Today, my day-to-day work as a **Data Scientist** involves **helping business unlock the potential hidden in their data** and help them take **critical, strategic decisions** that have far reaching, global influence on the organization.
    '''

    st.markdown(intro_body)
    st.link_button("Get in Touch! LinkedIn", "https://www.linkedin.com/in/naren-surampudi/")

    st.divider()

    st.header("Journey")

    with open('data/timeline.json', 'r') as f:
        timeline_data = f.read()
    timeline(timeline_data, height=400)

    st.divider()

    st.header("Skills")

    row1 = st.columns(4)
    row2 = st.columns(4)
    row3 = st.columns(4)

    skill_list = ["***Python***", "***AI & Machine Learning***", "***Data Science & Analyitcs***", "***Deep Learning***", "***Natural Language***",
    "***SQL***", "***PowerBI***", "***Pandas***", "***Dagster***", "***Streamlit***", "***Stakeholder Management***", "***Mentorship***"]

    i = 0
    for col in row1 + row2 + row3:
        tile = col.container(height=60, border=False)
        tile.button(skill_list[i])
        i += 1

    st.divider()

    st.header("Highlights")

    # col1.markdown("Incident-Outage forecating: 20pc avg reduction within teams adopting algorithm")
    # col1.markdown("Change Risk prediction: 30pc reduction in failed changes")
    # col1.markdown("Self-serve Analytics: 60pc increase in non-coders trying out advanced analytics")
    # col1.markdown("WPB SSP Data Transformation & Pipeline Automation: 80pc reduction in time spent on data operations")
    # col1.markdown("Risk Prioritization Framework: 60pc increased efficiency in driving prioritization of annual global budget for service sustainability")

    col1, col2 = st.columns(2)
    tile1 = col1.container(height=200, border=True)
    tile2 = col2.container(height=200, border=False)
    tile1.markdown("Built a machine learning pipeline to **predict risk of deployed changes** and reduce downtime due to failed changes. **Achieved signficant reduction in number of failed changes and downtime caused by failed changes**")
    tile2.metric(label="Failed Changes", value="Decreased", delta="-25%", delta_color="inverse")

    col3, col4 = st.columns(2)
    tile1 = col3.container(height=200, border=True)
    tile2 = col4.container(height=200, border=False)
    tile1.markdown("**Overhauled data operations and analytics** of WPB's SSP Program at HSBC through **reporting & data process enhancement and automation**. **Achieved massive reduction in time spent on data processes**")
    tile2.metric(label="Time to Report", value="Decreased", delta="-80%", delta_color="inverse")

    col5, col6 = st.columns(2)
    tile1 = col5.container(height=200, border=True)
    tile2 = col6.container(height=200, border=False)
    tile1.markdown("Built a **self-serve analytics platform** to drive **adoption of advanced analytics** amongst non-coder colleagues with minimal effort. **Witnessed increase in non-coders adopting advanced analytics to drive more in-depth reporting**")
    tile2.metric(label="Non-Coder Adoption of Advanced Analytics", value="Increased", delta="60%")

    col7, col8 = st.columns(2)
    tile1 = col7.container(height=200, border=True)
    tile2 = col8.container(height=200, border=False)
    tile1.markdown("Implemented **new ways of reporting** to drive **higher stakeholder engagement** across multiple workstreams in WPB. **Witnessed increased engagement from senior leadership and stakeholders, driving critical strategic and bussiness decisions**")
    tile2.metric(label="Stakeholder Engagement", value="Increased", delta="40%")

    col9, col10 = st.columns(2)
    tile1 = col9.container(height=200, border=True)
    tile2 = col10.container(height=200, border=False)
    tile1.markdown("Built a **machine learning pipeline** to **forecast incidents/outages** across the bank to mitigate negative impact of incidents/outages. **Achieved signficant reduction in incident/outage volume due to actions driven by forecast**")
    tile2.metric(label="Incident/Outage Volume", value="Decreased", delta="-15%", delta_color="inverse")

    style_metric_cards()

with tab2:

    with open("data/Naren Surampudi - Resume.pdf", "rb") as f:
        pdf_bytes = f.read()
    st.download_button("Download Resume", data=pdf_bytes, file_name='Naren Surampudi - Resume.pdf', mime='application/octet-stream')
    pdf_viewer(pdf_bytes)
