from pytube import YouTube

# create a YouTube object for the video you want to download
yt = YouTube("https://www.youtube.com/watch?v=fd3T8GTJmHA&list=PPSV")


# get the highest resolution video stream with both audio and video
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# set the download path to the current working directory
download_path = "./"

# download the video to the specified path
stream.download(download_path)
