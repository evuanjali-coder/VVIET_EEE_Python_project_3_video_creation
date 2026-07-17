from moviepy import VideoFileClip, AudioFileClip

def replace_audio(video_path, audio_path, output_video):

    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    final = video.with_audio(audio)

    final.write_videofile(output_video)

    return output_video
