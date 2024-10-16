import os
from pytube import YouTube
from pydub import AudioSegment


# Define the YouTube URL and times
youtube_url = "https://www.youtube.com/watch?v=FplVJuHl0p8"
start_time = 5  # in seconds
end_time = 26   # in seconds
output_filename = "trimmed_audio.mp3"

# Define output files
output_filename = 'yt_audio'

output_filepath = os.path.join('..','audio',output_filename)


# Download audio track from YouTube
def download_audio(youtube_url, start_time, end_time, output_filename):
    # Initialize YouTube object
    yt = YouTube(youtube_url)

    # Extract audio stream (selecting the highest quality audio stream)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio file
    audio_file = audio_stream.download(filename="full_audio.mp4")

    # Load the audio file using pydub
    audio = AudioSegment.from_file(audio_file)

    # Trim the audio from start_time to end_time
    trimmed_audio = audio[start_time*1000:end_time*1000]  # pydub works in milliseconds

    # Export the trimmed audio
    trimmed_audio.export(output_filename, format="mp3")
    print(f"Trimmed audio saved as: {output_filename}")


# Call the function to download and trim audio
download_audio(youtube_url, start_time, end_time, output_filepath)
