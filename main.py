from st_on_hover_tabs import on_hover_tabs
from streamlit_player import st_player
import streamlit as st

st.set_page_config(layout="wide")
with open("home.css", "r") as css_file:
    custom_css = css_file.read()

st.markdown('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />', unsafe_allow_html=True)
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
head1, head2 = st.columns([1,10])
with head1:
    st.image("./assets/images/logo.png", width=100)
with head2:
    st.markdown('<p class="custom-class">Nwitch</p>', unsafe_allow_html=True)
st.markdown('<style>' + open('style.css').read() +
            '</style>', unsafe_allow_html=True)



with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Trending', 'Category', 'Liked Videos', 'Watch Later', 'Playlist'],
                         iconName=['home', 'tag', 'category', 'thumb_up', 'smart_display', 'playlist_play'],
                         styles={'navtab': {'background-color': '#392e5c',
                                            'color': '#FFFFFF',
                                            'font-size': '18px',
                                            'transition': '.25s',
                                            'white-space': 'nowrap',
                                            'text-transform': 'uppercase'},
                                 'tabOptionsStyle': {':hover :hover': {'color': '#9146ff',
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
