import os
import whisper
from moviepy import VideoFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS

# Extract Audio
def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path


# Speech To Text
def speech_to_text(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]


# Translate Text
def translate_text(text, target_language):
    translated = GoogleTranslator(
        source='auto',
        target=target_language
    ).translate(text)
    return translated


# Generate AI Voice
def text_to_speech(text, language, output_file):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)
    return output_file


# Create Subtitle File
def create_subtitle(text, subtitle_file):

    with open(subtitle_file, "w", encoding="utf-8") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:10:00,000\n")
        f.write(text)

    return subtitle_file
