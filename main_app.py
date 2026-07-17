import os
import streamlit as st

from video_utils import *

st.set_page_config(page_title="AI Video Language Studio")

st.title("🎬 AI Video Language Studio")

uploaded_video = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov"]
)

language = st.selectbox(
    "Translate To",
    [
        "en",
        "hi",
        "kn",
        "ta",
        "te",
        "ml"
    ]
)

if uploaded_video:

    os.makedirs("temp", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    video_path = os.path.join(
        "temp",
        uploaded_video.name
    )

    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    st.video(video_path)

    if st.button("Start Processing"):

        st.write("Extracting Audio...")

        audio_path = "temp/audio.wav"
        extract_audio(video_path, audio_path)

        st.success("Audio Extracted")

        st.write("Speech To Text...")

        text = speech_to_text(audio_path)

        st.text_area(
            "Recognized Text",
            text,
            height=150
        )

        st.write("Translating...")

        translated = translate_text(
            text,
            language
        )

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )

        st.write("Generating AI Voice...")

        voice_path = "outputs/voice.mp3"

        text_to_speech(
            translated,
            language,
            voice_path
        )

        st.audio(voice_path)

        st.write("Generating Subtitle...")

        subtitle_path = "outputs/subtitles.srt"

        create_subtitle(
            translated,
            subtitle_path
        )

        st.success("Subtitle Created")

        st.download_button(
            "Download Subtitle",
            open(subtitle_path, "rb"),
            file_name="subtitles.srt"
        )

        st.download_button(
            "Download AI Voice",
            open(voice_path, "rb"),
            file_name="voice.mp3"
        )

        st.success("Project Completed Successfully!")
