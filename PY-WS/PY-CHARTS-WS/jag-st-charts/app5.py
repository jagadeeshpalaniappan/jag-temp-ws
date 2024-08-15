import pandas as pd
import streamlit as st
import streamlit_antd_components as sac
import temp_data as td

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


valid_tag_ids = {"temp_min", "temp_max", "wind"}

seattle_weather = pd.read_csv(
    "https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv",
    parse_dates=["date"],
)


if "template" not in st.session_state:
    st.session_state.template = td.template

if "selected_tags" not in st.session_state:
    st.session_state.selected_tags = []


def isValidTag(tagId):
    if tagId in valid_tag_ids:
        return True


def render_tags_tree():
    def get_asset_tree_items(assetId):
        asset = td.assetMap[assetId]
        return sac.TreeItem(
            asset["name"],
            icon="apple",
            children=[
                sac.TreeItem(
                    "All Tags",
                    children=map(lambda tag: sac.TreeItem(tag["id"]), asset["tags"]),
                ),
            ],
        )

    tree_items = map(
        get_asset_tree_items,
        td.selectedAssetIds,
    )

    selected_items = sac.tree(
        items=tree_items,
        # label="",
        index=[2],
        color="#4682b4",
        # width="350",
        # height=300,
        icon="table",
        open_all=True,
        checkbox=True,
    )
    selected_tags = list(filter(isValidTag, selected_items))
    st.session_state.selected_tags = selected_tags


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


def render_filters():
    st.session_state.filter1 = st.slider("Tag1", 200, 500, 250)


def render_settings():
    st.session_state.plot_height = st.slider("Chart Height", 200, 500, 250)


def render_charts():

    for chart in st.session_state.selected_tab["charts"]:
        with st.expander(chart["name"], True):

            st.line_chart(
                seattle_weather,
                x="date",
                y=st.session_state.selected_tags,
                height=st.session_state.plot_height,
            )


def render_right_side_panel():

    with st.expander("Tag Browser", True):
        render_tags_tree()
    with st.expander("Tag Expression", False):
        st.write("TODO")
        # render_tags_tree()
    with st.expander("Filter", False):
        render_filters()
    with st.expander("Settings", False):
        render_settings()


def render_main():
    render_tabs()
    render_charts()


def test():
    return ""


def main():
    test()
    st.header("jag-charts `beta`")
    col1, col2 = st.columns([3, 1])
    with col2.container():
        render_right_side_panel()
    with col1.container():
        render_main()


main()
