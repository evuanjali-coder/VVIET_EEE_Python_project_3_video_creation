import whisper
from moviepy import VideoFileClip, AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS
import subprocess


# Extract Audio
def extract_audio(video_path, audio_path):

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    return audio_path


# Speech to Text
def speech_to_text(audio_path):

    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    return result["text"]


# Translate
def translate_text(text, language):

    translated = GoogleTranslator(
        source="auto",
        target=language
    ).translate(text)

    return translated


# AI Voice
def generate_voice(text, language, output_audio):

    tts = gTTS(
        text=text,
        lang=language
    )

    tts.save(output_audio)

    return output_audio


# Subtitle File
def create_subtitle(text, subtitle_path):

    with open(subtitle_path, "w", encoding="utf-8") as file:

        file.write("1\n")
        file.write("00:00:00,000 --> 00:10:00,000\n")
        file.write(text)

    return subtitle_path


# Replace Audio
def replace_audio(video_path, audio_path, output_video):

    video = VideoFileClip(video_path)

    audio = AudioFileClip(audio_path)

    final = video.with_audio(audio)

    final.write_videofile(
        output_video,
        codec="libx264",
        audio_codec="aac"
    )

    return output_video


# Add Subtitle
def add_subtitle(video_path, subtitle_path, output_video):

    command = [
        "ffmpeg",
        "-y",
        "-i",
        video_path,
        "-vf",
        f"subtitles={subtitle_path}",
        output_video
    ]

    subprocess.run(command)

    return output_video
