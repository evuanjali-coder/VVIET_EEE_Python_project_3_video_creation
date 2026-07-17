import streamlit as st
import os

from video_utils import *

st.set_page_config(page_title="AI Video Language Studio")

st.title("🎬 AI Video Language Studio")

video = st.file_uploader(
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

if video:

    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    video_path = os.path.join(
        "temp",
        video.name
    )

    with open(video_path, "wb") as file:
        file.write(video.read())

    st.video(video_path)

    if st.button("Process Video"):

        st.write("Step 1 : Extracting Audio...")

        audio_path = "temp/audio.wav"

        extract_audio(
            video_path,
            audio_path
        )

        st.success("Audio Extracted")

        st.write("Step 2 : Speech To Text...")

        text = speech_to_text(audio_path)

        st.text_area(
            "Recognized Text",
            text
        )

        st.write("Step 3 : Translating...")

        translated = translate_text(
            text,
            language
        )

        st.text_area(
            "Translated Text",
            translated
        )

        st.write("Step 4 : AI Voice Generation...")

        voice = "output/voice.mp3"

        generate_voice(
            translated,
            language,
            voice
        )

        st.audio(voice)

        st.write("Step 5 : Subtitle Generation...")

        subtitle = "output/subtitle.srt"

        create_subtitle(
            translated,
            subtitle
        )

        st.success("Subtitle Created")

        st.write("Step 6 : Replacing Audio...")

        translated_video = "output/translated_video.mp4"

        replace_audio(
            video_path,
            voice,
            translated_video
        )

        st.write("Step 7 : Adding Subtitle...")

        final_video = "output/final_video.mp4"

        add_subtitle(
            translated_video,
            subtitle,
            final_video
        )

        st.success("Video Processing Completed")

        st.video(final_video)

        with open(final_video, "rb") as file:

            st.download_button(
                "Download Final Video",
                file,
                file_name="TranslatedVideo.mp4"
            )
