from st_on_hover_tabs import on_hover_tabs
from streamlit_player import st_player
import streamlit as st

st.set_page_config(layout="wide")

# header logo
st.image("./assets/images/logo.png", width=100)
st.markdown('<style>' + open('./style.css').read() +
            '</style>', unsafe_allow_html=True)

# sidebar
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

# video title function


def videoTitle(images, title, channel, views):
    st.markdown(
        f'<div style="display:flex;">'
        f'<div style="border-radius:50%; overflow: hidden; width: 50px; height: 50px;">'
        f'<img width="100%" src="{images}"/>'
        f'</div>'
        f'<div style="padding-left: 10px;"><h5 style="margin:0; padding:0;">{title}</h5><p style="color:gray; margin:0; padding:0;">{channel}</p><p style="color:gray; margin:0; padding:0;">{views}</p></div>'
        f'</div>',
        unsafe_allow_html=True
    )

# Main section


def Dashboard():
    video_url = "https://www.youtube.com/embed/gq2759kMojg?si=tOFwoQV2sXL7Vjom&autoplay=1&mute=1"
    st.markdown(
        f'<div style="position:relative;width:100%;height:50;padding-bottom:56.25%;"><iframe src="{video_url}" style="position:absolute;width:100%;height:100%;left:0;top:0;" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>', unsafe_allow_html=True)
    st.header("Related to your previous video")
    c1, c2, c3 = st.columns(3)
    c = st.empty()
    c.write("")
    with c1:
        st_player("https://www.youtube.com/watch?v=sHjtSotku2s&pp=ygUEdGVueg%3D%3D")
        videoTitle("https://yt3.ggpht.com/nrefx19H-uS5kwx-tSsTGju0hPqNj9VLRgo4elKpMbsrsnsDLHGqmV4wb_04Sp8voDPJVTppYg=s176-c-k-c0x00ffffff-no-rj-mo",
                   "18 Minutes of TenZ SHEESH Moments Highlights", "Tenz", "1,3 rb x ditonton 39 menit yang lalu")

    with c2:
        st_player("https://www.youtube.com/watch?v=Ux-oVjvumo8&pp=ygUEdGVueg%3D%3D")
        videoTitle("https://yt3.ggpht.com/nrefx19H-uS5kwx-tSsTGju0hPqNj9VLRgo4elKpMbsrsnsDLHGqmV4wb_04Sp8voDPJVTppYg=s176-c-k-c0x00ffffff-no-rj-mo",
                   "SEN TenZ SHOWS THE DIFFERENCE BETWEEN PRO & RADIANT", "Tenz", "314 rb x ditonton  1 bulan yang lalu")
    with c3:
        st_player("https://www.youtube.com/watch?v=OMhr6exAp_k&pp=ygUEdGVueg%3D%3D")
        videoTitle("https://yt3.ggpht.com/nrefx19H-uS5kwx-tSsTGju0hPqNj9VLRgo4elKpMbsrsnsDLHGqmV4wb_04Sp8voDPJVTppYg=s176-c-k-c0x00ffffff-no-rj-mo",
                   "WHEN TenZ PLAYS JETT AGAINST RADIANTS !!!", "Tenz", "614 rb x ditonton  9 bulan yang lalu")

    c.write("")
    st.header("Something that you like")
    c4, c5, c6 = st.columns(3)
    with c4:
        c = st.empty()
        c.write("")
        st_player(
            "https://www.youtube.com/watch?v=bA_2G5Xp2Ek&pp=ygUObW9iaWxlIGxlZ2VuZHM%3D")
        videoTitle("https://yt3.ggpht.com/ytc/APkrFKYdPqBBgHeGd60YLYu5JjfFAuzqgxxKdbHichsd=s48-c-k-c0x00ffffff-no-rj",
                   "THANK YOU HAJI PUTRA ", "XINNN", "614 rb x ditonton  9 bulan yang lalu")

    with c5:
        st_player(
            "https://www.youtube.com/watch?v=olJbt5w6fW4&pp=ygUObW9iaWxlIGxlZ2VuZHM%3D")
        videoTitle("https://yt3.ggpht.com/1JPtMOmKyatS7bR7ZM0iuE6mlAW9ySccfOTyYECriFy_2W_7YImdZQW_XuArztPmZNppn1uamQ=s48-c-k-c0x00ffffff-no-rj",
                   "Review Skin Starlight Arlott", "Jonathan Liandi", "159 rb x ditonton  4 jam yang lalu")

    with c6:
        st_player(
            "https://www.youtube.com/watch?v=msK3AbWWNy0&pp=ygUObW9iaWxlIGxlZ2VuZHM%3D")
        videoTitle("https://yt3.ggpht.com/ytc/APkrFKaey1Pcn9bgDxXDKmiHlyynt8JdI2L6z0TWimbZ9g=s48-c-k-c0x00ffffff-no-rj",
                   "CARA LAWAN META CIKI PAKE LANCELOT", "Jeje Adriel", "39 rb x ditonton  10 jam yang lalu")


def Movie():
    st.header("Movie that maybe you like")
    c1, c2, c3 = st.columns(3)
    c = st.empty()
    c.write("")
    with c1:
        st_player(
            "https://www.youtube.com/watch?v=bA_2G5Xp2Ek&pp=ygUObW9iaWxlIGxlZ2VuZHM%3D")
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
