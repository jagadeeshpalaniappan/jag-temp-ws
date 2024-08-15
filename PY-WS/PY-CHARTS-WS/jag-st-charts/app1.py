import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.header("jag-charts `beta`")


st.sidebar.subheader("Line chart parameters")

defaultSelectedTags = ["temp_min", "temp_max"]
tags = st.sidebar.multiselect(
    "Select Tags", ["temp_min", "temp_max", "wind"], defaultSelectedTags
)


plot_height = st.sidebar.slider("Specify plot height", 200, 500, 250)

st.sidebar.markdown(
    """
---
Created with ❤️ \n
by [Jagadeesh Palaniappan](https://www.linkedin.com/in/jagadeeshpalaniappan/)
"""
)

seattle_weather = pd.read_csv(
    "https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv",
    parse_dates=["date"],
)

# Row C
st.markdown("### TS chart 1")
st.line_chart(seattle_weather, x="date", y=tags, height=plot_height)
st.markdown("### TS chart 2")
st.line_chart(seattle_weather, x="date", y=tags, height=plot_height)
st.markdown("### TS chart 3")
st.line_chart(seattle_weather, x="date", y=tags, height=plot_height)
