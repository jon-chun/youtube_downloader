import os
import yt_dlp
from pydub import AudioSegment

# Define the YouTube URL and times
# Samuel L. Jackson Ezekiel
youtube_url = "https://www.youtube.com/watch?v=FplVJuHl0p8"
# Movie Preview Voiceover
youtube_url = "https://www.youtube.com/watch?v=qGBdwOsvl3E"

start_time = 40  # in seconds
end_time = 136   # in seconds
output_filename = "trimmed_audio_preview_voiceover.mp3"

output_filepath = os.path.join('..', 'audio', output_filename)

def download_audio(youtube_url, start_time, end_time, output_filename):
    # Set up yt-dlp options to download only the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'full_audio.%(ext)s',  # Save as full_audio.mp3
    }

    # Download the audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Load the downloaded audio file using pydub
    audio = AudioSegment.from_file("full_audio.mp3")

    # Trim the audio from start_time to end_time
    trimmed_audio = audio[start_time*1000:end_time*1000]  # pydub works in milliseconds

    # Export the trimmed audio
    trimmed_audio.export(output_filename, format="mp3")
    print(f"Trimmed audio saved as: {output_filename}")

# Call the function to download and trim the audio
download_audio(youtube_url, start_time, end_time, output_filepath)
