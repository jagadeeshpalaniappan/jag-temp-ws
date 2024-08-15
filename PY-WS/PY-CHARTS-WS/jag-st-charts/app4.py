import pandas as pd
import streamlit as st
import streamlit_antd_components as sac

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


valid_tag_ids = {"temp_min", "temp_max", "wind"}

seattle_weather = pd.read_csv(
    "https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv",
    parse_dates=["date"],
)


def isValidTag(tagId):
    if tagId in valid_tag_ids:
        return True


tabs = [
    {
        "name": "Tab 1",
        "charts": [
            {
                "name": "Chart 1",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 2",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 3",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 4",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 5",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
        ],
    },
    {
        "name": "Tab 2",
        "charts": [
            {
                "name": "Chart 1",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 2",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
        ],
    },
    {
        "name": "Tab 3",
        "charts": [
            {
                "name": "Chart 1",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 2",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
            {
                "name": "Chart 3",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
        ],
    },
    {
        "name": "Tab 4",
        "charts": [
            {
                "name": "Chart 1",
                "tags": [
                    {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                    {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                    {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                ],
            },
        ],
    },
]

st.session_state.template = {"tabs": tabs}


def render_tags_tree(key):
    selected_items = sac.tree(
        key=key,
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
                tag=[
                    sac.Tag("Tag", color="red"),
                    sac.Tag("Tag2A", color="cyan"),
                ],
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
                tag=[
                    sac.Tag("Tag", color="red"),
                    sac.Tag("Tag3A", color="cyan"),
                ],
                disabled=True,
            ),
        ],
        # label="",
        index=[2],
        color="#4682b4",
        # width="350",
        # height=300,
        icon="table",
        open_all=True,
        checkbox=True,
    )
    st.session_state.selected_tags = list(filter(isValidTag, selected_items))


def render_charts():
    no_charts = len(st.session_state.selected_tab["charts"])
    for chart in st.session_state.selected_tab["charts"]:
        with st.expander(chart["name"], True):
            st.line_chart(
                seattle_weather,
                x="date",
                y=st.session_state.selected_tags,
                height=st.session_state.plot_height,
            )


def render_tabs():
    tab_items = map(
        lambda tab: sac.TabsItem(
            label=tab["name"], icon="folder", tag=str(len(tab["charts"]))
        ),
        st.session_state.template["tabs"],
    )
    selected_tab_str = sac.tabs(
        tab_items,
        variant="outline",
        size="sm",
        color="#4682b4",
    )
    st.session_state.selected_tab = next(
        tab
        for tab in st.session_state.template["tabs"]
        if tab["name"] == selected_tab_str
    )
    # st.write(st.session_state.selected_tab)


def render_filters():
    st.session_state.filter1 = st.slider("Tag1", 200, 500, 250)


def render_settings():
    st.session_state.plot_height = st.slider("Chart Height", 200, 500, 250)


def render_right_side_panel():
    with st.expander("Tag Browser", True):
        render_tags_tree("Tag Browser")
    with st.expander("Tag Expression", False):
        render_tags_tree("Tag Expression")
    with st.expander("Filter", False):
        render_filters()
    with st.expander("Settings", False):
        render_settings()


def render_main():
    render_tabs()
    render_charts()


def main():
    st.header("jag-charts `beta`")
    col1, col2 = st.columns([3, 1])
    with col2.container():
        render_right_side_panel()
    with col1.container():
        render_main()


main()
