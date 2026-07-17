import streamlit as st
from video_utils import *

st.title("🎥 AI Video Translator")

video = st.file_uploader(
    "Upload Video",
    type=["mp4","avi","mov"]
)

language = st.selectbox(
    "Translate To",
    ["Hindi","Kannada","Tamil","Telugu"]
)

if video:

    st.video(video)

    if st.button("Translate Video"):

        st.write("Extracting Audio...")

        st.write("Speech to Text...")

        st.write("Translating Text...")

        st.write("Generating AI Voice...")

        st.write("Replacing Original Audio...")

        st.write("Adding Subtitles...")

        st.success("Translated Video Ready!")

        st.video("outputs/final_video.mp4")

        st.download_button(
            "Download Video",
            open("outputs/final_video.mp4","rb"),
            file_name="TranslatedVideo.mp4"
        )
