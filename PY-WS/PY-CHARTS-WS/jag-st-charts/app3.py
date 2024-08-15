import pandas as pd
import streamlit as st
import streamlit_antd_components as sac

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


seattle_weather = pd.read_csv(
    "https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv",
    parse_dates=["date"],
)
valid_tag_ids = {"temp_min", "temp_max", "wind"}


def isValidTag(tagId):
    if tagId in valid_tag_ids:
        return True


with st.sidebar.container():
    st.header("jag-charts `beta`")
    with st.expander("Tag Browser", True):
        selectedItems = sac.tree(
            items=[
                sac.TreeItem(
                    "Asset1",
                    icon="apple",
                    description="item description",
                    children=[
                        sac.TreeItem(
                            "All Tags",
                            children=[
                                sac.TreeItem("temp_min"),
                                sac.TreeItem("temp_max"),
                                sac.TreeItem("wind"),
                            ],
                        ),
                    ],
                ),
                sac.TreeItem(
                    "Asset2",
                    tag=[sac.Tag("Tag", color="red"), sac.Tag("Tag2A", color="cyan")],
                    children=[
                        sac.TreeItem(
                            "All Tags",
                            children=[
                                sac.TreeItem("Tag A"),
                                sac.TreeItem("Tag B"),
                                sac.TreeItem("Tag C"),
                            ],
                        ),
                        sac.TreeItem("tooltip", icon="github", tooltip="item tooltip"),
                    ],
                ),
                sac.TreeItem(
                    "Asset3",
                    tag=[sac.Tag("Tag", color="red"), sac.Tag("Tag3A", color="cyan")],
                    disabled=True,
                ),
            ],
            # label="",
            index=[2],
            color="#4682b4",
            width=250,
            height=300,
            icon="table",
            open_all=True,
            checkbox=True,
        )
        selectedTags = list(filter(isValidTag, selectedItems))
    with st.expander("Tag Expression", False):
        sac.tree(
            items=[
                sac.TreeItem(
                    "item1",
                    tag=[sac.Tag("Tag", color="red"), sac.Tag("Tag2", color="cyan")],
                ),
                sac.TreeItem(
                    "item2",
                    icon="apple",
                    description="item description",
                    children=[
                        sac.TreeItem("tooltip", icon="github", tooltip="item tooltip"),
                        sac.TreeItem(
                            "item2-2",
                            children=[
                                sac.TreeItem("item2-2-1"),
                                sac.TreeItem("item2-2-2"),
                                sac.TreeItem("item2-2-3"),
                            ],
                        ),
                    ],
                ),
                sac.TreeItem("disabled", disabled=True),
                sac.TreeItem(
                    "item3",
                    children=[
                        sac.TreeItem("item3-1"),
                        sac.TreeItem("item3-2"),
                    ],
                ),
            ],
            label="Exp",
            index=[2],
            color="#4682b4",
            width=250,
            height=300,
            icon="table",
            open_all=True,
            checkbox=True,
        )
    with st.expander("Filter", False):
        tag1Filter = st.slider("Tag1", 200, 500, 250)
    with st.expander("Settings", False):
        plot_height = st.slider("Chart Height", 200, 500, 250)


def main():
    st.write(selectedTags)
    with st.expander("TS chart 1", True):
        st.line_chart(seattle_weather, x="date", y=selectedTags, height=plot_height)
    with st.expander("TS chart 2", True):
        st.line_chart(seattle_weather, x="date", y=selectedTags, height=plot_height)
    with st.expander("TS chart 3", True):
        st.line_chart(seattle_weather, x="date", y=selectedTags, height=plot_height)


main()
