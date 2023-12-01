from st_on_hover_tabs import on_hover_tabs
from streamlit_player import st_player
import streamlit as st

st.set_page_config(layout="wide")
st.image("./assets/images/logo.png", width=100)
st.markdown('<style>' + open('./style.css').read() +
            '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Series', 'Movies'],
                         iconName=['dashboard', 'movie', 'people'],
                         styles={'navtab': {'background-color': '#111',
                                            'color': '#818181',
                                            'font-size': '18px',
                                            'transition': '.3s',
                                            'white-space': 'nowrap',
                                            'text-transform': 'uppercase'},
                                 'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                       'cursor': 'pointer'}},
                                 'iconStyle': {'position': 'fixed',
                                               'left': '7.5px',
                                               'text-align': 'left'},
                                 'tabStyle': {'list-style-type': 'none',
                                              'margin-bottom': '30px',
                                              'padding-left': '30px'}},
                         default_choice=0)


def Dashboard():
    st.header("Related to your previous video")
    c1, c2, c3 = st.columns(3)
    c = st.empty()
    c.write("")
    with c1:
        st_player("https://www.youtube.com/watch?v=sHjtSotku2s&pp=ygUEdGVueg%3D%3D")
    with c2:
        st_player("https://www.youtube.com/watch?v=Ux-oVjvumo8&pp=ygUEdGVueg%3D%3D")
    with c3:
        st_player("https://www.youtube.com/watch?v=OMhr6exAp_k&pp=ygUEdGVueg%3D%3D")

    c.write("")
    st.header("Something that you like")
    c4, c5, c6 = st.columns(3)
    with c4:
        c = st.empty()
        c.write("")
        st.image("./assets/images/tenz1.png")

    with c5:
        st.image("./assets/images/tenz2.png")
    with c6:
        st.image("./assets/images/tenz1.png")


def Movie():
    st.header("Movie that maybe you like")
    c1, c2, c3 = st.columns(3)
    c = st.empty()
    c.write("")
    with c1:
        st_player("https://www.youtube.com/watch?v=43xSX4_tjkM&pp=ygUFbW92aWU%3D")
    with c2:
        st_player("https://www.youtube.com/watch?v=JXcMu0jmeQQ&pp=ygUFbW92aWU%3D")
    with c3:
        st_player("https://www.youtube.com/watch?v=OMhr6exAp_k&pp=ygUEdGVueg%3D%3D")

    c.write("")
    st.header("Something that you like")
    c4, c5, c6 = st.columns(3)
    with c4:
        c = st.empty()
        c.write("")
        st.image("./assets/images/tenz1.png")

    with c5:
        st.image("./assets/images/tenz2.png")
    with c6:
        st.image("./assets/images/tenz1.png")


def Series():
    st.header("Series that maybe you like")
    c1, c2, c3 = st.columns(3)
    c = st.empty()
    c.write("")
    with c1:
        st_player("https://www.youtube.com/watch?v=43xSX4_tjkM&pp=ygUFbW92aWU%3D")
    with c2:
        st_player("https://www.youtube.com/watch?v=JXcMu0jmeQQ&pp=ygUFbW92aWU%3D")
    with c3:
        st_player("https://www.youtube.com/watch?v=OMhr6exAp_k&pp=ygUEdGVueg%3D%3D")

    c.write("")
    st.header("Something that you like")
    c4, c5, c6 = st.columns(3)
    with c4:
        c = st.empty()
        c.write("")
        st.image("./assets/images/tenz1.png")

    with c5:
        st.image("./assets/images/tenz2.png")
    with c6:
        st.image("./assets/images/tenz1.png")


if 'Dashboard' in tabs:
    Dashboard()
elif 'Movies' in tabs:
    Movie()
elif 'Series' in tabs:
    Series()
else:
    Dashboard()
