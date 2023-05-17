import youtube_dl

# create a dictionary with the options for the download
options = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
}

# create a YouTubeDL object and pass the options
with youtube_dl.YoutubeDL(options) as ydl:
    # download the video using its URL
    ydl.download(['https://www.youtube.com/watch?v=2Gg6Seob5Mg&list=PLGmxyVGSCDKvmLInHxJ9VdiwEb82Lxd2E'])
