import streamlit as st
from streamlit_timeline import timeline
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
import base64
import requests
import json

st.set_page_config(page_title='Welcome!', layout='wide')


# with open('images/self_image.png', "rb") as f:
#     data = f.read()
#     encoded = base64.b64encode(data)

# with open('images/self_image_encoded', 'wb') as f:
#     f.write(encoded)

# with open('images/self_image_encoded', 'rb') as f:
#     image_data = f.read()

image_data = requests.get("https://github.com/nsurampu/Portfolio/blob/main/images/self_image_encoded")
print(image_data.text['raw_lines'])
image_data = "data:image/png;base64," + image_data#.decode("utf-8")
with st.sidebar:
    card(title="Get in touch!", text="LinkedIn", url="https://www.linkedin.com/in/naren-surampudi/", image=image_data,
        styles={
            "card": {
                "width": "100%"
            }
        }
    )

st.header("Hi, I'm Naren Surampudi!")

intro_body = '''
And I like to refer to myself as an accidental data professional. Why is that? Well, I wasn't a big fan of numbers and math during my schooling days; I did love coding though, starting
as early as 6th grade. If you had told my school-boy self that one day he would be working with math and numbers day-in and day-out, I'd bet he'd be quite shocked (and maybe a little bit crestfallen).\n
Then how did I land up in this space? Well, I first fell in love with all things **Data**, **AI** and **Machine Learning** during college, when I came across a simple tutorial for predicting house prices. Looking back, it was
a really simple thing, but at that time, it blew my mind. I could never have imagined being able to predict stuff, but more importantly, drive critical decisions that could potentially have far-reaching impact. That took me down the data
rabbit hole that I doubt I'll try to get out of anytime soon.\n
Today, my day-to-day work as a **Data Scientist** involves **helping business unlock the potential hidden in their data** and help them take **critical, strategic decisions** that have far reaching, global influence on the organization.
'''

st.markdown(intro_body)

st.divider()

with open('data/timeline.json', 'r') as f:
    timeline_data = f.read()
timeline(timeline_data, height=400)

st.divider()

st.header("Skills")

row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)

skill_list = ["**Python**", "**AI & Machine Learning**", "**Data Science & Analyitcs**", "**Deep Learning**", "**Natural Language**",
"**SQL**", "**PowerBI**", "**Pandas**", "**Dagster**", "**Streamlit**", "**Stakeholder Management**", "**Mentorship**"]

# col1.button("Python")
# col2.button("AI & Machine Learning")
# col3.button("Data Science & Analytics")
# col4.button("Deep Learning")
# col5.button("Natural Language")

# col1.button("SQL")
# col2.button("PowerBI")
# col3.button("Pandas")
# col4.button("Dagster")
# col5.button("Streamlit")

# col1.button("Project Management")
# col2.button("Stakeholder Management")
# col3.button("Mentorship")

i = 0
for col in row1 + row2 + row3:
    tile = col.container(height=60)
    tile.markdown(skill_list[i])
    i += 1

st.divider()

st.header("Highlights")

# col1.markdown("Incident-Outage forecating: 20pc avg reduction within teams adopting algorithm")
# col1.markdown("Change Risk prediction: 30pc reduction in failed changes")
# col1.markdown("Self-serve Analytics: 60pc increase in non-coders trying out advanced analytics")
# col1.markdown("WPB SSP Data Transformation & Pipeline Automation: 80pc reduction in time spent on data operations")
# col1.markdown("Risk Prioritization Framework: 60pc increased efficiency in driving prioritization of annual global budget for service sustainability")

col1, col2 = st.columns(2)
tile1 = col1.container(height=190)
tile2 = col2.container(height=190)
tile1.markdown("Built a machine learning pipeline to **predict risk of deployed changes**, to drive reduction downtime caused by deployment of poor quality changes. **Achieved signficant reduction in number of failed changes and downtime caused by failed changes**")
tile2.metric(label="Failed Changes", value="Decreased", delta="-25%", delta_color="inverse")

col3, col4 = st.columns(2)
tile1 = col3.container(height=190)
tile2 = col4.container(height=190)
tile1.markdown("Overhauled data operations and analytics of Wealth & Personal Banking IT's Service Sustainability Program through enhanced reporting & data process enhancement and automation. **Achieved massive reduction in time spent on data processes, consquently enhancing productivity and opening opportunities for more advanced reporting & analytics**")
tile2.metric(label="Time to Report", value="Decreased", delta="-80%", delta_color="inverse")

col5, col6 = st.columns(2)
tile1 = col5.container(height=190)
tile2 = col6.container(height=190)
tile1.markdown("Built a self-serve analytics pipeline to drive adoption of advanced analytics amongst non-coder colleagues with minimal effort. **Witnessed increase in non-coders adopting advanced analytics to drive more in-depth reporting, consquently increasing analytics quality**")
tile2.metric(label="Non-Coder Adoption of Advanced Analytics", value="Increased", delta="60%")

col7, col8 = st.columns(2)
tile1 = col7.container(height=190)
tile2 = col8.container(height=190)
tile1.markdown("Implemented new ways of reporting to drive higher senior stakeholder engagement across multiple workstreams under Wealth & Personal Banking IT. **Witnessed increased engagement from senior leadership and stakeholders, driving critical strategic and bussiness decisions**")
tile2.metric(label="Stakeholder Engagement", value="Increased", delta="40%")

col9, col10 = st.columns(2)
tile1 = col9.container(height=190)
tile2 = col10.container(height=190)
tile1.markdown("Built a machine learning pipeline to **forecast incidents/outages** across the bank, to drive proactive behaviour and mitigate negative impact of incidents/outages. **Achieved signficant reduction in incident/outage volume due to actions driven by forecast**")
tile2.metric(label="Incident/Outage Volume", value="Decreased", delta="-15%", delta_color="inverse")

style_metric_cards()
