# YouTube Downloader

Here's an outline of options to download videos and audio tracks from YouTube, along with associated Python library options and combinations, in GitHub Markdown format:

# YouTube Download Options

## Video Downloads

### 1. pytube
- Lightweight, dependency-free library
- Supports both video and audio downloads
- Easy to use API

```python
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
yt.streams.filter(progressive=True, file_extension='mp4').first().download()
```

### 2. youtube-dl
- Feature-rich command-line program
- Can be used as a Python module
- Supports many video hosting platforms

```python
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
```

### 3. yt-dlp
- Fork of youtube-dl with additional features and fixes
- Faster downloads and more frequent updates

```python
import yt_dlp

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
```

## Audio Downloads

### 1. pytube (audio only)
```python
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
yt.streams.filter(only_audio=True).first().download()
```

### 2. youtube-dl (audio only)
```python
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
```

### 3. yt-dlp (audio only)
```python
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])
```

## Combination Libraries

### 1. pafy + youtube-dl
- pafy provides a convenient API
- youtube-dl handles the actual downloading

```python
import pafy

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video = pafy.new(url)
best = video.getbest()
best.download()
```

### 2. moviepy + youtube-dl
- moviepy for video editing capabilities
- youtube-dl for downloading

```python
from moviepy.editor import *
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'])

video = VideoFileClip("video.mp4")
# Perform editing operations with moviepy
```

## Note
- Always respect copyright laws and YouTube's terms of service when downloading content.
- Some of these libraries may require additional dependencies like FFmpeg for full functionality.
- Consider using official APIs or YouTube Premium for legitimate access to content when possible.

Citations:
[1] https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/
[2] https://dev.to/ethand91/download-youtube-videos-with-python-4kp4
[3] https://dev.to/kalebu/how-to-download-youtube-video-as-audio-using-python-33g9
[4] https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/
[5] https://github.com/whitehatboy005/Youtube-audio-and-video-Downloader
[6] https://speechify.com/blog/youtube-audio-downloader/
[7] https://www.youtube.com/watch?v=01Dg6iBUbQ8
[8] https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97?gi=58dbae910f3d
[9] https://fireflies.ai/blog/download-audio-from-youtube
[10] https://clipchamp.com/en/blog/download-youtube-videos/
[11] https://www.pcmag.com/how-to/how-to-download-youtube-videos
