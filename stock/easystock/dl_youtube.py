from pytube import YouTube

# Specify the URL of the YouTube video
url = 'https://www.youtube.com/watch?v=c6Cjo4LeY5A'

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print(f'Video downloaded: {yt.title}')
