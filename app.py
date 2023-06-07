import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="pyurhost.com", page_icon=":globe_with_meridians:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_zeus = Image.open("images/zeus.webp")
img_titan = Image.open("images/titan.webp")
img_spartan = Image.open("images/spartan.webp")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("pyurhost.com")
    st.title("we are pyurhost.com")
    st.write(
        "Providing the oppertunity for people to enjoy minecraft together is our passion."
    )
    st.write("[Learn More >](shop.pyurhost.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Sergey Gruzdov (Owner): what i do")
        st.write("##")
        st.write(
            """
            I like to think of myself not as an owner of a company but simply as a Sysadmin that likes to provide people with high quality minecraft servers.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- Plans ----
with st.container():
    st.write("---")
    st.header("Our Plans")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
#Titan
    with image_column:
        st.image(img_titan)
    with text_column:
        st.subheader("Titan Plan")
        st.write(
            """
        Zeus Plan: 8GB of RAM,
                   50 Player slots,
                   15 Euro per month
            """
        )
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
#Zeus
    with image_column:
        st.image(img_zeus)
    with text_column:
        st.subheader("Zeus")
        st.write(
            """
        Zeus Plan: 5GB of RAM,
                   30 Player slots,
                   10 Euro per month,

            """
        )
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
#Spartan
    with image_column:
        st.image(img_spartan)
    with text_column:
        st.subheader("Spartan")
        st.write(
            """
        Zeus Plan: 2GB of RAM,
                   10 Player slots,
                   5 Euro per month,
            """
        )


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sergey@gruzdov.dev" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

